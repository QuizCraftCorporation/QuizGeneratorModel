import logging
import time
from .models.MCQ_generator import MCQGenerator
from .utils.text_splitter import TextSplitter
from .utils.file_reader import FileReader
from .containers.nagim_quiz import NagimQuiz

class QuizGenerator():
    """
    Class that have behaviour for quiz generation. It uses different models.
    In this version of class it uses only ChatGPT.
    """

    def __init__(self, debug=False) -> None:
        """
        Loads all models and intialize splitter.
        """

        # Addition questions in case of failing to achieve 'max_questions' number.
        self.questions_buffer = []

        if debug:
            logging.basicConfig(level=logging.INFO)
       
        self.MCQ_model = MCQGenerator()        
        self.text_splitter = TextSplitter()

        logging.info("Initialization complete.")

    def create_quiz_from_files(self, file_paths: list[str], max_questions=-1) -> list:
        """
        Create quiz from specified files.

        Args:
            file_paths (list[str]): Path to files for quiz generation.
            max_questions (int): Maximum number of questions in resulting quiz. If -1 then no upper bound for question number.

        Returns:
            list: A list with questions. Check README.md to see format.
        """
        questions_per_file = -1
        if max_questions != -1:
            questions_per_file = max_questions // len(file_paths)

        complex_quiz = []
        for file_path in file_paths:
            logging.info(f"PROCESSING FILE {file_path}")
            text_data = FileReader(file_path).get_content()
            complex_quiz += self.create_questions(text_data, questions_per_file)
        
        if len(complex_quiz) < max_questions:
            logging.info("Not enough questions for complex quiz. Using buffer...")
            flat_buffer = self._flat_questions_buffer()
            complex_quiz += flat_buffer[:max_questions-len(complex_quiz)]
        
        self.questions_buffer = []
        return complex_quiz

    def create_questions(self, text: str, max_questions: int) -> list:
        """
        Create quiz from plain text.

        Args:
            text (list[str]): Text for quiz generation.
            max_questions (int): Maximum number of questions in resulting quiz. If -1 then no upper bound for question number.

        Returns:
            list: A list with questions. Check README.md to see format.
        """
        
        # Check for errors.
        if type(max_questions) != int:
            raise Exception("max_questions parameter must be int!")
        if max_questions != -1 and max_questions < 0:
            raise Exception(f"max_questions={max_questions} is invalid value!")

        #Splitting text
        logging.info("Splitting text")
        text_chunks = self.text_splitter.split_text(text)
        logging.info(f"Text splitted into {len(text_chunks)} chunks")

        # Calculating questions per chunk number.
        questions_per_chunk = -1
        if max_questions != -1:
            questions_per_chunk = max(max_questions // len(text_chunks), 1)

        logging.info(f"Start processing text chunks. Number of chunks is {len(text_chunks)}.")

        # Quiz generation.
        quiz = []
        for i in range(len(text_chunks)):
            questions = self._create_question_chunk(text_chunks[i], questions_per_chunk)
            logging.info(f"{i+1} of {len(text_chunks)} chunks scanned!")
            logging.info(f"Add {len(questions)} new questions!")
            quiz += questions
            if len(quiz) >= max_questions and max_questions != -1:
                logging.info(f"Quiz already has enough questions - {max_questions}. Finish generation.")
                return quiz
            if i < len(text_chunks) - 1:
                time.sleep(10)
        
        # Adding questions from buffer.
        if len(quiz) < max_questions:
            logging.info(f"Not enough questions were generated. Using question buffer...")
            flat_buffer = self._flat_questions_buffer()
            quiz += flat_buffer[:max_questions-len(quiz)]
            self.questions_buffer = []
        
        return quiz
    
    def _create_question_chunk(self, text_chunk: str, number_of_questions: int):
        """
        Create a single chunk of questions.
        """
        
        questions = self.MCQ_model.generate_question_chunk(text_chunk)
        if number_of_questions != -1:
            if len(questions) > number_of_questions:
                logging.info(f"Saving {number_of_questions-len(questions)} questions into a buffer.")
                self.questions_buffer.append(questions[number_of_questions-len(questions):])
                questions = questions[:number_of_questions]
                
        return questions

    def _flat_questions_buffer(self) -> list:
        """
        Converet 2D question buffer to 1D with follow of importance order.
        """
        if len(self.questions_buffer) == 0:
            return []
        
        flat_buffer = []
        max_chunk_size = max([len(question_chunk) for question_chunk in self.questions_buffer])

        for j in range(0, max_chunk_size):
            for question_chunk in self.questions_buffer:
                if j < len(question_chunk):
                    flat_buffer.append(question_chunk[j])
        
        return flat_buffer

import logging
import time
from .models.MCQ_generator import MCQGenerator
from .utils.text_splitter import TextSplitter
from .utils.file_reader import FileReader
from .containers.nagim_quiz import NagimQuiz
from .containers.nagim_question import NagimQuestion
from .containers.question_buffer import QuestionBuffer

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
        self.questions_buffer = QuestionBuffer()

        if debug:
            logging.basicConfig(level=logging.INFO)
       
        self.MCQ_model = MCQGenerator()        
        self.text_splitter = TextSplitter()

        logging.info("Initialization complete.")

    def create_quiz_from_files(self, file_paths: list[str], max_questions: int = None) -> NagimQuiz:
        """
        Create quiz from specified files.

        Args:
            file_paths (list[str]): Path to files for quiz generation.
            max_questions (int): Maximum number of questions in resulting quiz. If -1 then no upper bound for question number.

        Returns:
            list: A list with questions. Check README.md to see format.
        """
        # Check for errors.

        if max_questions != None and type(max_questions) != int:
            raise Exception("max_questions parameter must be int!")
        if max_questions != None and max_questions < 0:
            raise Exception(f"max_questions={max_questions} is invalid value!")
        

        questions_per_file = None
        if max_questions != None:
            questions_per_file = max_questions // len(file_paths)

        complex_quiz = NagimQuiz()
        for file_path in file_paths:
            logging.info(f"PROCESSING FILE {file_path}")
            text_data = FileReader(file_path).get_content()
            complex_quiz = complex_quiz.union(self._create_quiz(text_data, questions_per_file))
        
        if max_questions != None and len(complex_quiz) < max_questions:
            logging.info("Not enough questions for complex quiz. Using buffer...")
            n = max_questions - len(complex_quiz)
            complex_quiz.add_questions(self.questions_buffer.get_best_questions(n))
        
        self.questions_buffer.clear()
        return complex_quiz

    def _create_quiz(self, text: str, max_questions: int = None) -> NagimQuiz:
        """
        Create quiz from plain text.

        Args:
            text (list[str]): Text for quiz generation.
            max_questions (int): Maximum number of questions in resulting quiz. If -1 then no upper bound for question number.

        Returns:
            list: A list with questions. Check README.md to see format.
        """

        #Splitting text
        logging.info("Splitting text")
        text_chunks = self.text_splitter.split_text(text)
        logging.info(f"Text splitted into {len(text_chunks)} chunks")

        # Calculating questions per chunk number.
        questions_per_chunk = None
        if max_questions != None:
            questions_per_chunk = max(max_questions // len(text_chunks), 1)

        logging.info(f"Start processing text chunks. Number of chunks is {len(text_chunks)}.")

        # Quiz generation.
        quiz = NagimQuiz()
        for i in range(len(text_chunks)):
            questions = self._create_question_chunk(text_chunks[i], questions_per_chunk)
            quiz.add_questions(questions)
            
            logging.info(f"{i+1} of {len(text_chunks)} chunks scanned!")
            logging.info(f"Add {len(questions)} new questions!")
            
            if max_questions != None and len(quiz) >= max_questions:
                logging.info(f"Quiz already has enough questions - {len(quiz)} out of {max_questions}. Finish generation.")
                return quiz
            
            if i < len(text_chunks) - 1:
                time.sleep(10)
        
        # Adding questions from buffer.
        if max_questions != None and len(quiz) < max_questions:
            logging.info(f"Not enough questions were generated. Using question buffer...")
            n = max_questions - len(quiz)
            quiz.add_questions(self.questions_buffer.get_best_questions(n))
        
        return quiz
    
    def _create_question_chunk(self, text_chunk: str, number_of_questions: int = None) -> list[NagimQuestion]:
        """
        Create a single chunk of questions.
        """
        
        questions = self.MCQ_model.generate_question_chunk(text_chunk)
        if number_of_questions != None:
            questions = self.questions_buffer.divide_chunk(questions, number_of_questions)
                
        return questions

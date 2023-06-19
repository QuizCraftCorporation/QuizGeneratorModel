import logging
from .models.MCQ_generator import MCQGenerator
from .utils.text_splitter import TextSplitter
from .utils.file_reader import FileReader
import time

class QuizGenerator():

    def __init__(self, debug=False) -> None:
        """
        Loads all models and intialize splitter.
        """
        
        if debug:    
            logging.basicConfig(level=logging.INFO)

        logging.info("Loading models into RAM...")       
        self.MCQ_model = MCQGenerator()
        logging.info("Models loaded succesfully")
        
        self.text_splitter = TextSplitter()



    def create_questions_from_files(self, file_paths: list[str]):
        """
        Create questions from specified files.
        """
        complex_quiz = []
        for file_path in file_paths:
            logging.info(f"PROCESSING FILE {file_path}")
            text_data = FileReader(file_path).get_content()
            complex_quiz += self.create_questions(text_data)
        return complex_quiz

    def create_questions(self, text: str):
        """
        Create questions from plain text.
        """
        
        logging.info("Splitting text")
        text_chunks = self.text_splitter.split_text(text)
        logging.info(f"Text splitted into {len(text_chunks)} chunks")

        result = []
        logging.info(f"Start processing text chunks. Number of chunks is {len(text_chunks)}.")
        for i in range(len(text_chunks)):
            try:
                questions = self.MCQ_model.generate_question(text_chunks[i])
                logging.info(f"{i+1} of {len(text_chunks)} chunks scanned!")
                logging.info(f"Add {len(questions)} new questions!")
                result += questions
                time.sleep(10)
            except:
                logging.info("Failed to parse cluster of questions :c")
                continue

        return result

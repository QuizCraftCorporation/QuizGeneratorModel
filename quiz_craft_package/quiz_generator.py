import logging
from langchain.chat_models import ChatOpenAI
from .models.MCQ_generator import MCQGenerator
from .utils.text_splitter import TextSplitter
from .utils.file_reader import FileReader
import time

class QuizGenerator():

    def __init__(self, q_fraction = [0.7, 0.2, 0.1], debug=False) -> None:
        """
        Loads all models and intialize splitter.
        """
        
        if debug:    
            logging.basicConfig(level=logging.INFO)

        logging.info("Loading models into RAM...")
        OPEN_AI_KEY = "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" 
        language_model = ChatOpenAI(openai_api_key=OPEN_AI_KEY, temperature=0, model="gpt-3.5-turbo")      
        self.MCQ_model = MCQGenerator(language_model)
        
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
            questions = self.MCQ_model.generate_question(text_chunks[i])
            logging.info(f"{i+1} of {len(text_chunks)} chunks scanned!")
            logging.info(f"Add {len(questions)} new questions!")
            result += questions
            time.sleep(10)

        return result

from utils.text_splitter import TextSplitter
from utils.file_reader import FileReader
from models.questions_generator_model import QuestionsGeneratorModel
import logging


def generate_quiz(filepath: str, debug: bool = False):
    if debug:    
        logging.basicConfig(level=logging.INFO)
    
    text_data = FileReader(filepath).get_content()
    model = QuestionsGeneratorModel()
    splitter = TextSplitter(text_data)
    text_chunks = splitter.text_chunks


    return model.create_questions(text_chunks)


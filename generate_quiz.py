from text_splitter import TextSplitter
from models.questions_generator_model import QuestionsGeneratorModel
import logging


def generate_quiz(text_data: str, debug: bool = False):
    if debug:    
        logging.basicConfig(level=logging.INFO)
    
    model = QuestionsGeneratorModel()
    splitter = TextSplitter(text_data)
    text_chunks = splitter.text_chunks


    return model.create_questions(text_chunks)


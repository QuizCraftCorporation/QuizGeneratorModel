from utils.text_splitter import TextSplitter
from utils.file_reader import FileReader
from models.questions_generator_model import QuestionsGeneratorModel
from transformers import AutoTokenizer
import logging


def generate_quiz(filepath: str, debug: bool = False):
    if debug:    
        logging.basicConfig(level=logging.INFO)
    
    common_tokenizer = AutoTokenizer.from_pretrained("./resources/t5MCQ_gen/")
    text_data = FileReader(filepath).get_content()
    model = QuestionsGeneratorModel()
    splitter = TextSplitter(text_data, common_tokenizer)
    text_chunks = splitter.text_chunks


    return model.create_questions(text_chunks)


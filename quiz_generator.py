import logging
from models.MCQ_generator import MCQGenerator
from utils.text_splitter import TextSplitter
from utils.file_reader import FileReader


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
        
        self.text_splitter = TextSplitter(self.MCQ_model.create_tokenizer)



    def create_questions_from_file(self, file_path: str):
        """
        Create questions from specified file.
        """
        
        text_data = FileReader(file_path).get_content()
        return self.create_questions(text_data)

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
                question = self.MCQ_model.generate_question(text_chunks[i])
                if len(question[1]) < 2:
                    logging.info(f"Failed to generate question number - {i+1}. Not enough options.")
                    continue
                logging.info(f"{i+1} of {len(text_chunks)} questions are generated!")
                result.append(question)
            except:
                continue

        return result
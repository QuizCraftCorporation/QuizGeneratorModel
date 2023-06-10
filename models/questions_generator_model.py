import logging
from models.MCQ_generator import MCQGenerator

class QuestionsGeneratorModel():

    def __init__(self) -> None:
        self.MCQ_model = MCQGenerator()
        
    def create_questions(self, text_chunks: list[str]):
        result = []
        logging.info(f"Start processing text chunks. Number of chunks is {len(text_chunks)}.")
        for i in range(len(text_chunks)):
            try:
                questions = self.MCQ_model.generate_questions(text_chunks[i])
                logging.info(f"{i+1} of {len(text_chunks)} questions are generated!")
                result.append(questions)
            except:
                continue

        return result
import os
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI
from ..containers.nagim_question import NagimQuestion

class MCQGenerator:
    """
    Class for models that generates MCQ questions.
    """

    def __init__(self) -> None:
        """
        Initialize MCQ Generator model.
        """
 
        self.llm = ChatOpenAI(openai_api_key=os.environ["OPEN_AI_TOKEN"], temperature=0, model="gpt-3.5-turbo", request_timeout=70, max_retries=2)
        self.instruction = """
            I want you to create several multiple choice questions based on text provided by user.
            Send questions in order of importance and quality. The first questions are the most important for the given text and have good quality, and the last ones are not as good as the first ones.
            Strictly follow python-like format:
            ["Which data types in C requires 4 bytes of memory?", ["int", "short int", "char", "float"], ["int", "float"]]
            ["Who was the first astronaut?", ["Neil Armstrong", "Yuri Gagarin", "Elon Musk", "Xi Jinping"], ["Neil Armstrong"]]
        """

    def generate_question_chunk(self, text: str) -> list[NagimQuestion]:
        """
        Generate a chunk of questions.

        Args:
            text (str): Reference text.
        
        Returns:
            list[NagimQuestion]: Question chunk.
        """
        
        output = self.llm([SystemMessage(content=self.instruction), HumanMessage(content=text)])
        #print(output.content)
        output = output.content.replace("\n\n", "\n").split("\n")
        questions = []
        for question_raw in output:
            try:
                raw_question_list = eval(question_raw)
                questions.append(NagimQuestion.from_array(raw_question_list))
            except:
                continue
        return questions
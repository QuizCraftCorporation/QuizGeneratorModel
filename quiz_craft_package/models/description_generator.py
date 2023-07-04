import os
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI
from ..containers.nagim_quiz import NagimQuiz

class DescriptionGenerator:
    """
    Class for models that generates description for quizzes.
    """

    def __init__(self) -> None:
        """
        Initialize Description Generator model.
        """
 
        self.llm = ChatOpenAI(openai_api_key=os.environ["OPEN_AI_TOKEN"], temperature=0, model="gpt-3.5-turbo")
        self.instruction = """
            You will get the quiz text. Please generate a description for it.
            Put your description between "" brackets.
        """

    def generate_description(self, quiz: NagimQuiz) -> NagimQuiz:
        """
        Generate a description for quiz.
        """

        text = str(quiz)
        output = self.llm([SystemMessage(content=self.instruction), HumanMessage(content=text)])
        print(output.content)
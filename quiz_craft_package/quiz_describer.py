import os
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI
from .containers.nagim_quiz import NagimQuiz
from .utils.text_splitter import TextSplitter

class QuizDescriber:
    """
    Class for models that generates description for quizzes.
    """

    def __init__(self) -> None:
        """
        Initialize Description Generator model.
        """
 
        self.llm = ChatOpenAI(openai_api_key=os.environ["OPEN_AI_TOKEN"], temperature=0, model="gpt-3.5-turbo")
        self.instruction = """
            You will get the quiz text. Describe what this quiz is about.
            Maximum length of description is 5 sentences.
        """
        self.text_splitter = TextSplitter()

    def generate_description(self, quiz: NagimQuiz) -> NagimQuiz:
        """
        Generate a description for quiz.
        """

        # To not allow large texts
        text = self.text_splitter.cut_by_tokens(str(quiz), 3500)
        output = self.llm([SystemMessage(content=self.instruction), HumanMessage(content=text)])
        quiz.set_description(output.content)
        return quiz
import os
import time
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI
from .containers.nagim_quiz import NagimQuiz
from .utils.text_splitter import TextSplitter

class QuizCategorizer:
    """
    Class for models classify complexity of quizzes.
    """

    def __init__(self) -> None:
        """
        Initialize quiz classification model.
        """
 
        self.llm = ChatOpenAI(openai_api_key=os.environ["OPEN_AI_TOKEN"], temperature=0, model="gpt-3.5-turbo")
        self.instruction = """
            You are quiz classifier. You will get the quiz text.
            Respond with one number./
            1 - if quiz is for kids./
            2 - if quiz is for students./
            3 - if quiz is for professionals./
            RESPOND WITH 1 NUMBER.
        """
        self.text_splitter = TextSplitter()

    def classify_quiz(self, quiz: NagimQuiz) -> int:
        """
        Classify the complexity of quiz from 1 to 3. Where 1 - kid's quiz, 2 - student's quiz, 3 - proffesional's quiz

        Args:
            quiz (NagimQuiz): Quiz for classification.

        Returns:
            int: Complexity of quiz [1-3].
        """

        # To not allow large texts
        start_time = time.time()
        text = self.text_splitter.cut_by_tokens(str(quiz), 3500)
        output = self.llm([SystemMessage(content=self.instruction), HumanMessage(content=text)])
        quiz_complexity = int(output.content)
        elapsed_time = time.time() - start_time
        time.sleep(max(21-elapsed_time, 0.0))
        return quiz_complexity
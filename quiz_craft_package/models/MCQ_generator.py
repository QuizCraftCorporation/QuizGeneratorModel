from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI


class MCQGenerator:
    def __init__(self) -> None:
        OPEN_AI_KEY = "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" 
        self.llm = ChatOpenAI(openai_api_key=OPEN_AI_KEY, temperature=0, model="gpt-3.5-turbo")
        self.instruction = """
            Create Multiple choice question.
            Respond in format:
            Question
            A: Answer A
            B: Answer B
            C: Answer C
            D: Answer D
        """

    def generate_question(self, text: str):
        output = self.llm([HumanMessage(content=self.instruction + text)])
        output = output.content.split("\n")
        question = output[0]
        options = [output[1][3:], output[2][3:], output[3][3:], output[4][3:]]
        return [question, options]

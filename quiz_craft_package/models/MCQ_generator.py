from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI


class MCQGenerator:
    def __init__(self) -> None:
        OPEN_AI_KEY = "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" 
        self.llm = ChatOpenAI(openai_api_key=OPEN_AI_KEY, temperature=0, model="gpt-3.5-turbo")
        self.instruction = """
            You are multiple choice question generator. You will get text from user and you must create multiple choice questions based on text provided by user.
            Questions should be based on what the text is about, not how the author writes it. Questions should test knowledge of what the text is trying to teach the reader.
            Respond in python array like style where first element is question itself then subarray contains options to answer and last element is subarray that has indexes of right answers of options in first subarray.
            Example:
            ["Question text", ["option A", "option B", "option C", "option D"], [0, 2]]
        """

    def generate_question(self, text: str):
        output = self.llm([SystemMessage(content=self.instruction), HumanMessage(content=text)])
        #print(output.content)
        output = output.content.split("\n")
        questions = []
        for question_raw in output:
            questions.append(eval(question_raw))
        return questions

from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI


class MCQGenerator:
    def __init__(self) -> None:
        OPEN_AI_KEY = "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" 
        self.llm = ChatOpenAI(openai_api_key=OPEN_AI_KEY, temperature=0, model="gpt-3.5-turbo")
        self.instruction = """
            You are multiple choice question generator. You will get text from user and you must create multiple choice questions based on text provided by user.
            Questions should be based on what the text is about, not how the author writes it. Questions should test knowledge of what the text is trying to teach the reader.
            Strictly respond in format and do not add extra line breaks (If you can make more than one question start each question in a new line):
            Question text
            A: Answer A
            B: Answer B
            C: Answer C
            D: Answer D (You can add more options if required just add other english alphabet letters)
            Answer: AB (enumerate all right answer letters without spaces or write just 1 letter if only 1 answer is true)
        """

    def generate_question(self, text: str):
        output = self.llm([SystemMessage(content=self.instruction), HumanMessage(content=text)])
        #print(output.content)
        output = output.content.split("\n\n")
        questions = []
        for question_raw in output:
            question_splitted = question_raw.split("\n")
            question = question_splitted[0]
            options = []
            for i in range(1, len(question_splitted)-1):
                options.append(question_splitted[i][3:])
            questions.append([question, options])
        return questions

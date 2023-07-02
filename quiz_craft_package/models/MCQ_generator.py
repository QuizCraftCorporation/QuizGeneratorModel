from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI


class MCQGenerator:
    """
    Class for models that generates MCQ questions.
    """

    def __init__(self) -> None:
        """
        Initialize MCQ Generator model.
        """
        
        OPEN_AI_KEY = "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" 
        self.llm = ChatOpenAI(openai_api_key=OPEN_AI_KEY, temperature=0, model="gpt-3.5-turbo")
        self.instruction = """
            I want you to create several multiple choice questions based on text provided by user.
            Send questions in order of importance and quality. The first questions are the most important for the given text and have good quality, and the last ones are not as good as the first ones.
            Strictly follow python-like format:
            ["Which data types in C requires 4 bytes of memory?", ["int", "short int", "char", "float"], ["int", "float"]]
            ["Who was the first astronaut?", ["Neil Armstrong", "Yuri Gagarin", "Elon Musk", "Xi Jinping"], ["Neil Armstrong"]]
        """

    def generate_question_chunk(self, text: str) -> list:
        """
        Generate a chunk of questions.
        """
        
        output = self.llm([SystemMessage(content=self.instruction), HumanMessage(content=text)])
        #print(output.content)
        output = output.content.replace("\n\n", "\n").split("\n")
        questions = []
        for question_raw in output:
            try:
                generated_question = eval(question_raw)
                if self._check_if_question_is_valid(generated_question):
                    index_array = [generated_question[1].index(answer) for answer in generated_question[2]]
                    generated_question[2] = index_array
                    questions.append(generated_question)
                else:
                    continue
            except:
                continue
        return questions

    def _check_if_question_is_valid(self, question: list):
        """
        Check if the question format is correct.
        """
        
        if type(question) is list:
            if len(question) == 3:
                if type(question[0]) is str and type(question[1]) is list and type(question[2]) is list:
                    if len(question[1]) >= len(question[2]):
                        for answer in question[2]:
                            if answer not in question[1]:
                                return False
                        return True
        return False

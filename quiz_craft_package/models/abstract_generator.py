from langchain.schema import HumanMessage, SystemMessage


class AbstractGenerator:
    def __init__(self, language_model) -> None:
        self.llm = language_model
        self.instruction = """
            You are helpful assistant
        """

    def generate_question(self, text: str):
        output = self.llm([SystemMessage(content=self.instruction), HumanMessage(content=text)])
        #print(output.content)
        output = output.content.replace("\n\n", "\n").split("\n")
        questions = []
        for question_raw in output:
            try:
                generated_question = eval(question_raw)
                if self._check_if_question_is_valid(generated_question):
                    questions.append(generated_question)
                else:
                    continue
            except:
                continue
        return questions

    def _check_if_question_is_valid(self, question: list):
        return True
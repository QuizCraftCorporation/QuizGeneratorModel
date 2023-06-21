from langchain.schema import HumanMessage, SystemMessage


class BooleanQGenerator:
    def __init__(self, language_model) -> None:
        self.llm = language_model
        self.instruction = """
            You are boolean question generator. You will get text from user and you must create true/false questions based on text provided by user.
            Questions should be based on what the text is about, not how the author writes it. Questions should test knowledge of what the text is trying to teach the reader.
            Questions must have the simple answer like just true or false.
            Strictly respond in python array like style where first element is a question itself, second elements is the answer to question which is True or False python boolean.
            Separate each your question arrays with one line break and make sure that each of them can be executed in python by eval()
            Example:
            ["Question text", True]
        """

    def generate_question(self, text: str):
        output = self.llm([SystemMessage(content=self.instruction), HumanMessage(content=text)])
        print(output.content)
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
        if type(question) is list:
            if len(question) == 3:
                if type(question[0]) is str and type(question[1]) is list and type(question[2]) is list:
                    if len(question[1]) >= len(question[2]):
                        if max(question[2]) < len(question[1]) and min(question[2]) > -1:
                            return True
        return False
from .abstract_generator import AbstractGenerator


class OpenQGenerator(AbstractGenerator):
    def __init__(self, language_model) -> None:
        super().__init__(language_model)
        self.instruction = """
            You are open ended-question generator. You will get text from user and you must create open-ended questions based on text provided by user.
            Questions should be based on what the text is about, not how the author writes it. Questions should test knowledge of what the text is trying to teach the reader.
            Open ended questions must require descreptive answer not just 1 word.
            Strictly respond in python array like style where first element is a question itself, second element is an example of answer on open-ended question.
            Separate each your question arrays with one line break and make sure that each of them can be executed in python by eval()
            Example:
            ["Question text", "Descreptive answer"]
        """

    def _check_if_question_is_valid(self, question: list):
        if type(question) is list:
            if len(question) == 2:
                if type(question[0]) is str and type(question[1]) is str:
                    return True
        return False
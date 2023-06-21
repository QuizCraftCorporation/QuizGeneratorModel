from .abstract_generator import AbstractGenerator

class BooleanQGenerator(AbstractGenerator):
    def __init__(self, language_model) -> None:
        super().__init__(language_model)
        self.instruction = """
            You are boolean question generator. You will get text from user and you must create true/false questions based on text provided by user.
            Questions should be based on what the text is about, not how the author writes it. Questions should test knowledge of what the text is trying to teach the reader.
            Questions must have the simple answer like just true or false.
            Strictly respond in python array like style where first element is a question itself, second elements is the answer to question which is True or False python boolean.
            Separate each your question arrays with one line break and make sure that each of them can be executed in python by eval()
            Example:
            ["Question text", True]
        """
    
    def _check_if_question_is_valid(self, question: list):
        if type(question) is list:
            if len(question) == 2:
                if type(question[0]) is str and type(question[1]) is bool:
                    return True
        return False
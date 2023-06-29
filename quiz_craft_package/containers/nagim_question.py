class NagimQuestion:
    """
    Class that contains question and operations over it.
    """
    
    def __init__(self, question_text: str, answers: list[str], right_answers: list[str]) -> None:
        self._question_text = question_text
        self._answers = answers
        self._right_answers = right_answers
        self._check_is_valid()
        
        self._right_answers_indexes = [answers.index(right_answer) for right_answer in right_answers]

    @property
    def question_text(self) -> str:
        return self._question_text

    @property
    def right_answers(self) -> list[str]:
        return self._right_answers

    @property
    def right_answers_indexes(self) -> list[int]:
        return self._right_answers_indexes
    
    @property
    def question_type():
        return "MCQ" # Not implemented yet.

    def _check_is_valid(self) -> None:
        if type(self._question_text) != str:
            raise Exception("Parameter 'question_text' must be string!")
        
        if type(self._answers) != list:
            raise Exception("Parameter 'answers' must be list of string!")
        
        if type(self._right_answers) != list:
            raise Exception("Parameter 'right_answers' must be list of string!")
        
        for right_answer in self._right_answers:
            if not right_answer in self._answers:
                raise Exception(f"Right answer '{right_answer}' is not presented among answers")
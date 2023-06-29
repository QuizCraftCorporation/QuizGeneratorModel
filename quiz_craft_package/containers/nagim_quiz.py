from .nagim_question import NagimQuestion

class NagimQuiz:
    """
    Class that quiz question and operations over it.
    """
    
    def __init__(self, questions: list[NagimQuestion] = []) -> None:
        self._questions = questions.copy()

    def get_question(self, index: int):
        return self._questions[index]

    def add_questions(self, questions: list[NagimQuestion]):
        self._questions += questions.copy()

    def union(self, quiz):
        merged_quiz = NagimQuiz()
        merged_questions = self._questions + quiz._questions
        merged_quiz.add_questions(merged_questions)
        return merged_quiz
    
    @staticmethod
    def from_string(str_data: str):
        questions_raw = str_data.split("\n\n")
        questions = []
        for question in questions_raw:
            if question == "":
                break
            questions.append(NagimQuestion.from_string(question))
        return NagimQuiz(questions=questions)

    def __len__(self):
        return len(self._questions)

    def __iter__(self):
        for question in self._questions:
            yield question

    def __str__(self):
        str_quiz = ""
        for question in self._questions:
            str_quiz += str(question) + "\n"
        return str_quiz
    
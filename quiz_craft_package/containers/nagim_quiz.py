from .nagim_question import NagimQuestion

class NagimQuiz:
    """
    Class that quiz question and operations over it.
    """
    
    def __init__(self) -> None:
        self._questions: list[NagimQuestion] = []

    def get_question(self, index: int):
        return self._questions[index]

    def add_questions(self, questions: list[NagimQuestion]):
        self._questions += questions

    def union(self, quiz):
        merged_quiz = NagimQuiz()
        merged_questions = self._questions + quiz._questions
        merged_quiz.add_questions(merged_questions)
        return merged_quiz

    def __len__(self):
        return len(self._questions)

    def __iter__(self):
        for question in self._questions:
            yield question

    

    
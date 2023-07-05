from .nagim_question import NagimQuestion

class NagimQuiz:
    """
    Class that contain quiz questions and operations over it.

    Attributes:
        description (str): Description of quiz. Empty by default.
    """
    
    def __init__(self, questions: list[NagimQuestion] = []) -> None:
        self._questions = questions.copy()
        self._description = ""

    def get_question(self, index: int) -> NagimQuestion:
        """
        Get question by index.

        Args:
            index (int): Index of question.
            
        Returns:
            NagimQuestion: Question.
        """
        
        return self._questions[index]

    def add_questions(self, questions: list[NagimQuestion]):
        """
        Add list of questions to quiz.

        Args:
            questions (list[Questions]): List of instances of NagimQuestion class.
        """
        
        self._questions += questions.copy()

    def union(self, quiz) -> object:
        """
        Create union with another quiz.

        Args:
            quiz (NagimQuiz): Quiz to merge with.
            
        Returns:
            NagimQuiz: Merged quiz.
        """
        merged_quiz = NagimQuiz()
        merged_questions = self._questions + quiz._questions
        merged_quiz.add_questions(merged_questions)
        return merged_quiz
    
    def set_description(self, description: str):
        """
        Add description to quiz.

        Args:
            description (str): Description for quiz.
        """
        self._description = description
        
    @property
    def description(self):
        return self._description

    @staticmethod
    def from_string(str_data: str) -> object:
        """
        Create quiz from string.

        Args:
            str_data (str): Quiz in string format.

        Returns:
            NagimQuiz: Quiz.
        """
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
    
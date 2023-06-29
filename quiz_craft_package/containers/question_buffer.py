from .nagim_question import NagimQuestion

class QuestionBuffer:
    """
    Class that keep best questions in order for future usage.
    """

    def __init__(self) -> None:
        self._question_chunks: list[list[NagimQuestion]] = []


    def _flatten(self) -> list[NagimQuestion]:
        """
        Converet 2D question buffer to 1D with follow of importance order.
        """
        if len(self._question_chunks) == 0:
            return []
        
        buffer = []
        max_chunk_size = max([len(question_chunk) for question_chunk in self._question_chunks])

        for j in range(0, max_chunk_size):
            for question_chunk in self._question_chunks:
                if j < len(question_chunk):
                    buffer.append(question_chunk[j])
        
        return buffer

    def get_best_questions(self, k: int) -> list[NagimQuestion]:
        return self._flatten()[:k]

    def divide_chunk(self, question_chunk: list[NagimQuestion], extract_count: int) -> list[NagimQuestion]:
        return_questions = question_chunk[:extract_count]
        self._question_chunks.append(question_chunk[extract_count-len(question_chunk):])

        return return_questions
    
    def clear(self):
        self._question_chunks = []
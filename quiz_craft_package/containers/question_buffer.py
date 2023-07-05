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
            
        Returns:
            list[NagimQuestion]: 1-d list of questions sorted by importance.
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
        """
        Get best k questions.

        Args:
            k (int): Maximum number of best questions to return.
            
        Returns:
            list[NagimQuestion]: Top k best questions list.
        """
        return self._flatten()[:k]

    def divide_chunk(self, question_chunk: list[NagimQuestion], extract_count: int) -> list[NagimQuestion]:
        """
        Divide chunk into buffer part and extract part. Use it if you want to buffer part of questions for future utilization.

        Args:
            question_chunk (list[NagimQuestion]): Chunk of questions.
            extract_count (int): How much questions must be in extract part.
            
        Returns:
            list[NagimQuestion]: Extract part of questions.
        """
        
        if len(question_chunk) < extract_count:
            return question_chunk
        
        return_questions = question_chunk[:extract_count]
        self._question_chunks.append(question_chunk[extract_count-len(question_chunk):])

        return return_questions
    
    def clear(self):
        """
        Clear question buffer.
        """
        self._question_chunks = []
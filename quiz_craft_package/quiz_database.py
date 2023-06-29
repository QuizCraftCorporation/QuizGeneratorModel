import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

class QuizDataBase:
    """
    Class for searching quizzes among saved ones.
    """

    def __init__(self, save_folder_path: str) -> None:
        OPEN_AI_KEY = "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"
        self.embeddings = OpenAIEmbeddings(openai_api_key=OPEN_AI_KEY)
        self.db = None
        self.save_folder_path = save_folder_path
        if os.path.exists(os.path.join(save_folder_path, "index.faiss")):
            self.db = FAISS.load_local(save_folder_path, self.embeddings)

    def save_quiz(self, quiz: list) -> None:
        """
        Save a quiz into vector database.
        """
        quiz_full_text = str(quiz)

        if self.db == None:
            self.db = FAISS.from_texts([quiz_full_text], self.embeddings)
        else:
            self.db.add_texts([quiz_full_text])
        
        self.db.save_local(self.save_folder_path)

    def search_quiz(self, query: str, number_of_results=4) -> list:
        """
        Perform a search inside a vector database to retrieve quiz.
        """
        docs = self.db.similarity_search(query, k=number_of_results)
        the_most_similar_quizzes = []
        for search_result in docs:
            the_most_similar_quizzes = eval(search_result.page_content)
        return the_most_similar_quizzes


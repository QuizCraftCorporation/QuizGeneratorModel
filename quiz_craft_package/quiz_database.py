import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from .containers.nagim_quiz import NagimQuiz

class QuizDataBase:
    """
    Class for searching quizzes among saved ones.
    """

    def __init__(self, save_folder_path: str) -> None:
        self.embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPEN_AI_TOKEN"])
        self.db = None
        self.save_folder_path = save_folder_path
        if os.path.exists(os.path.join(save_folder_path, "index.faiss")):
            self.db = FAISS.load_local(save_folder_path, self.embeddings)

    def save_quiz(self, quiz: NagimQuiz) -> None:
        """
        Save a quiz into vector database.
        """
        quiz_full_text = str(quiz)

        if self.db == None:
            self.db = FAISS.from_texts([quiz_full_text], self.embeddings)
        else:
            self.db.add_texts([quiz_full_text])
        
        self.db.save_local(self.save_folder_path)

    def search_quiz(self, query: str, number_of_results=4) -> list[NagimQuiz]:
        """
        Perform a search inside a vector database to retrieve quiz.
        """
        docs = self.db.similarity_search(query, k=number_of_results)
        the_most_similar_quizzes = []
        for doc in docs:
            the_most_similar_quizzes.append(NagimQuiz.from_string(doc.page_content))
        return the_most_similar_quizzes


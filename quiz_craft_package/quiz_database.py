import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document
from .containers.nagim_quiz import NagimQuiz

class QuizDataBase:
    """
    Class for searching quizzes among saved ones.
    """

    def __init__(self, save_folder_path: str) -> None:
        """
        Creates QuizDatabase instance.

        Args:
            save_folder_path (str): Folder to save cache of quizzes.
        """
        self.embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPEN_AI_TOKEN"])
        self.db = None
        self.save_folder_path = save_folder_path

    def save_quiz(self, quiz: NagimQuiz, unique_id: str) -> None:
        """
        Save a quiz into vector database.

        Args:
            quiz (NagimQuiz): Quiz to save.
            unique_id (str): Some unique string to identify your quiz while search.
        """
        if not os.path.exists(os.path.join(self.save_folder_path, "index.faiss")):
            raise Exception("Cannot search database is empty")
        
        self.db = FAISS.load_local(self.save_folder_path, self.embeddings)

        quiz_full_text = str(quiz)
        new_doc = Document(page_content=quiz_full_text, metadata=dict(unique_id=unique_id))

        self.db.add_documents([new_doc])
        
        self.db.save_local(self.save_folder_path)

    def search_quiz(self, query: str, number_of_results: int=4) -> list[tuple[NagimQuiz, str]]:
        """
        Perform a search inside a vector database to retrieve quiz.

        Args:
            query (str): Search query.
            number_of_results (int): Maximum number of quizzes to return.

        Returns:
            list[tuple[NagimQuiz,str]]: A list with quizzes that are the most appropriate to search query with unique id.
        """

        if not os.path.exists(os.path.join(self.save_folder_path, "index.faiss")):
            raise Exception("Cannot search database is empty")
        
        self.db = FAISS.load_local(self.save_folder_path, self.embeddings)

        docs = self.db.similarity_search(query, k=number_of_results)
        the_most_similar_quizzes = []
        for doc in docs:
            quiz = NagimQuiz.from_string(doc.page_content)
            the_most_similar_quizzes.append((quiz, doc.metadata["unique_id"]))
        return the_most_similar_quizzes


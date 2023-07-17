import json
import os
import requests
from .containers.nagim_quiz import NagimQuiz

class QuizDataBase:
    """
    Class for searching quizzes among saved ones.
    """
    def __init__(self, database_address: str) -> None:
        """
        Creates QuizDatabase instance.

        Args:
            database_address (str): Address to remote database.
        """
        self.db_address = database_address

    def save_quiz(self, quiz: NagimQuiz, unique_id: str) -> None:
        """
        Save a quiz into vector database.

        Args:
            quiz (NagimQuiz): Quiz to save.
            unique_id (str): Some unique string to identify your quiz while search.
        """
        quiz_full_text = str(quiz)
        quiz_data = {}
        quiz_data["raw_quiz_data"] = quiz_full_text
        quiz_data["unique_id"] = unique_id
        result = requests.post(self.db_address + "/save", json=quiz_data)
        if json.loads(result.text)["operation"] != "SUCCESS":
            raise Exception("Failed to save quiz. Error in database")

    def search_quiz(self, query: str, number_of_results: int=4) -> list[tuple[NagimQuiz, str]]:
        """
        Perform a search inside a vector database to retrieve quiz.

        Args:
            query (str): Search query.
            number_of_results (int): Maximum number of quizzes to return.

        Returns:
            list[tuple[NagimQuiz,str]]: A list with quizzes that are the most appropriate to search query with unique id.
        """
        top_similar_quizzes = []

        search_query = {}
        search_query["query"] = query
        search_query["number_of_results"] = number_of_results
        result = requests.post(self.db_address + "/search", json=search_query)
        response = json.loads(result.text)
        if response["operation"] == "EMPTY":
            raise Exception("Cannot search in empty database")
        
        for quiz_raw in response["payload"]:
            top_similar_quizzes.append(("", quiz_raw["unique_id"]))

        return top_similar_quizzes

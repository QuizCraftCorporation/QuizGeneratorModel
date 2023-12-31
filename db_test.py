from quiz_craft_package.quiz_database import QuizDataBase
from quiz_craft_package.containers.nagim_quiz import NagimQuiz

database = QuizDataBase("http://127.0.0.1:1234")

# result_file = open("./output/hitler.txt", "r", encoding="utf8")
# hitler = NagimQuiz.from_string(result_file.read())
# result_file.close()

# result_file = open("./output/music.txt", "r", encoding="utf8")
# music = NagimQuiz.from_string(result_file.read())
# result_file.close()

# result_file = open("./output/operation_systems.txt", "r", encoding="utf8")
# os_quiz = NagimQuiz.from_string(result_file.read())
# result_file.close()

# database.save_quiz(hitler, "hitler")
# database.save_quiz(os_quiz, "os")
# database.save_quiz(music, "music")

result = database.search_quiz("computer", number_of_results=3)
print(result)

#print(result[0][0])
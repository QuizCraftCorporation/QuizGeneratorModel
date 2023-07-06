from quiz_craft_package.quiz_categorizer import QuizCategorizer
from quiz_craft_package.containers.nagim_quiz import NagimQuiz


result_file = open("./output/fairy_tale.txt", "r", encoding="utf8")
fairy_tale = NagimQuiz.from_string(result_file.read())
result_file.close()

# result_file = open("./output/music.txt", "r", encoding="utf8")
# music = NagimQuiz.from_string(result_file.read())
# result_file.close()

# result_file = open("./output/operation_systems.txt", "r", encoding="utf8")
# os_quiz = NagimQuiz.from_string(result_file.read())
# result_file.close()

categorizer = QuizCategorizer()

complexity = categorizer.classify_quiz(fairy_tale)
print("COMPLEXITY:")
print(complexity)
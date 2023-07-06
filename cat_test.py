from quiz_craft_package.quiz_categorizer import QuizCategorizer
from quiz_craft_package.containers.nagim_quiz import NagimQuiz


result_file = open("./output/hitler.txt", "r", encoding="utf8")
hitler = NagimQuiz.from_string(result_file.read())
result_file.close()

# result_file = open("./output/music.txt", "r", encoding="utf8")
# music = NagimQuiz.from_string(result_file.read())
# result_file.close()

# result_file = open("./output/operation_systems.txt", "r", encoding="utf8")
# os_quiz = NagimQuiz.from_string(result_file.read())
# result_file.close()

categorizer = QuizCategorizer()

complexity = categorizer.classify_quiz(hitler)
print("COMPLEXITY:")
print(complexity)
from pprint import pprint
from quiz_craft_package.quiz_generator import QuizGenerator
from quiz_craft_package.stream_quiz_generator import StreamQuizGenerator

MATERIAL_TEXT_FILE_PATH = "./data/material.txt"
MATERIAL_TEXT_FILE_PATH_2 = "./data/material_2.txt"
RESULT_FILE_PATH = "./output/result.txt"

output_str = ""
q_gen = StreamQuizGenerator([MATERIAL_TEXT_FILE_PATH], debug=True, q_fraction=[0.34, 0.33, 0.33])
for question_pack in q_gen:
    for question in question_pack:
        output_str += str(question) + "\n"

result_file = open(RESULT_FILE_PATH, "w", encoding="utf8")
result_file.write(output_str)
result_file.close()

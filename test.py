from quiz_craft_package.quiz_generator import QuizGenerator

MATERIAL_TEXT_FILE_PATH = "./data/material.txt"
MATERIAL_TEXT_FILE_PATH_2 = "./data/material_2.txt"
RESULT_FILE_PATH = "./output/result.txt"

q_gen = QuizGenerator(debug=True)
result = q_gen.create_quiz_from_files([MATERIAL_TEXT_FILE_PATH, MATERIAL_TEXT_FILE_PATH_2], max_questions=9)

result_file = open(RESULT_FILE_PATH, "w", encoding="utf8")
result_file.write(str(result))
result_file.close()

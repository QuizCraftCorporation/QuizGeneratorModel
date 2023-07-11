from quiz_craft_package.quiz_stream_generator import QuizStreamGenerator
MATERIAL_TEXT_FILE_PATH = "./data/fairy_tale.txt"
MATERIAL_TEXT_FILE_PATH_2 = "./data/material_2.txt"
RESULT_FILE_PATH = "./output/fairy_tale.txt"

q_gen = QuizStreamGenerator(debug=False)

result = None
for quiz, i, n in q_gen.create_quiz_from_files([MATERIAL_TEXT_FILE_PATH], max_questions=3):
    result = quiz
    print(f"Scanned {i} out of {n}")

for question in result:
    print(str(question))

result_file = open(RESULT_FILE_PATH, "w", encoding="utf8")
result_file.write(str(result))
result_file.close()

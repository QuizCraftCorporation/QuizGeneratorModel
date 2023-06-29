from quiz_craft_package.quiz_generator import QuizGenerator

MATERIAL_TEXT_FILE_PATH = "./data/material.txt"
MATERIAL_TEXT_FILE_PATH_2 = "./data/material_2.txt"
RESULT_FILE_PATH = "./output/result.txt"

q_gen = QuizGenerator(debug=True)
result = q_gen.create_questions_from_files([MATERIAL_TEXT_FILE_PATH])

print(result)

output_str = ""
for q in result:
    output_str += q[0] + '\n'
    output_str += '|'.join(q[1]) + '\n'
    output_str += str(q[2]) + "\n"
    output_str += '\n\n'

result_file = open(RESULT_FILE_PATH, "w", encoding="utf8")
result_file.write(output_str)
result_file.close()

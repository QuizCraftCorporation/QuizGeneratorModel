from generate_quiz import generate_quiz

MATERIAL_TEXT_FILE_PATH = "./data/material.txt"
RESULT_FILE_PATH = "./output/result.txt"

material_file = open(MATERIAL_TEXT_FILE_PATH, "r", encoding="utf-8")
material_text = material_file.read()
material_file.close()

result = generate_quiz(material_text, debug=True)

output_str = ""
for q in result:
    output_str += q[0] + '\n'
    output_str += '|'.join(q[1])
    output_str += '\n\n'

result_file = open(RESULT_FILE_PATH, "w", encoding="utf8")
result_file.write(output_str)
result_file.close()

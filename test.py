from generate_quiz import generate_quiz
from utils.file_reader import FileReader

MATERIAL_TEXT_FILE_PATH = "./data/example.pdf"
RESULT_FILE_PATH = "./output/result.txt"

result = generate_quiz(MATERIAL_TEXT_FILE_PATH, debug=True)

output_str = ""
for q in result:
    output_str += q[0] + '\n'
    output_str += '|'.join(q[1])
    output_str += '\n\n'

result_file = open(RESULT_FILE_PATH, "w", encoding="utf8")
result_file.write(output_str)
result_file.close()

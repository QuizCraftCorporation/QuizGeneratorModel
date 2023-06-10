from material_processor import MaterialProcessor
from question_generator import TutorialGeneratorModel
import logging

logging.basicConfig(level=logging.INFO)

MATERIAL_TEXT_FILE_PATH = "./data/material.txt"
RESULT_FILE_PATH = "./output/result.txt"


model = TutorialGeneratorModel()
text_processeor = MaterialProcessor(MATERIAL_TEXT_FILE_PATH)
text_chunks = text_processeor.text_data
result = model.create_tutorial(text_chunks)

output_str = ""
for q in result:
    output_str += q[0] + '\n'
    output_str += '|'.join(q[1])
    output_str += '\n\n'

result_file = open(RESULT_FILE_PATH, "w", encoding="utf8")
result_file.write(output_str)
result_file.close()

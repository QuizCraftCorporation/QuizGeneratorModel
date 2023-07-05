# Quiz Generation model
## Installation

1. Clone repository
```console
git clone https://github.com/QuizCraftCorporation/QuizGeneratorModel.git
```

2. Create virtual environment and activate it
```console
python -m venv venv
```
(windows)
```console
venv\Scripts\activate
```
3. Install all dependencies
```console
pip install -r requirements.txt
```

## How to use
### Quiz generation

```python
# If you save everything in folder QuizGeneratorModel
# If not then use from folder_name.quiz_generator import QuizGenerator
from QuizGeneratorModel.quiz_craft_package.quiz_generator import QuizGenerator

quiz_gen = QuizGenerator(debug=False)
# Set debug=True if you want to see generation progress logs.

# RETURN VALUE IS 'NagimQuiz'
result = quiz_gen.create_questions_from_file(["path/to/text1.txt", "path/to/text2.pdf"], max_questions=10)
# Argument is a list of files
# Max questions is an upper bound on number of questions inside a generated quiz.
# Support .pdf and .txt at this moment.

```
### Quiz search
```python
from QuizGeneratorModel.quiz_craft_package.quiz_database import QuizDataBase

# Creates database for quizzes that automaticly caches loaded quizzes. Required for cosine search.
database = QuizDataBase("path/to/vector_db_cache_saving")

# Save quizzes in vector database
# quiz is 'NagimQuiz' object!
# The second argument is a unique string to distinguish the same quizzes form different authors.
database.save_quiz(quiz1, "Author: Ivan, ID:123")
database.save_quiz(quiz2, "Author: Ivan, ID:321")
database.save_quiz(quiz3, "Author: Petya, ID:123")

# RESULT IS A LIST of '(NagimQuiz, unique_id)' tuples
result = database.search_quiz("German war", number_of_results=3)
# First argument is a search query
# Second is a number of top most similar quizzes to show.
```

### Description generation
```python
from QuizGeneratorModel.quiz_craft_package.quiz_describer import QuizDescriber

describer = QuizDescriber()

# quiz is NagimQuiz object
describer.generate_description(quiz)
print(quiz.description) # Output description
```
## Quiz objects
### NagimQuiz
Class that contain quiz questions and operations over it.
```python
from QuizGeneratorModel.quiz_craft_package.containers.nagim_quiz import NagimQuiz

quiz = NagimQuiz.from_string("...")

# Iterate through each question
for question in quiz:
    print(str(question)) # question is 'NagimQuestion' object

# Get number of questions
print(len(quiz))

# Get specific question
print(quiz.get_question(0))

# Can be converted to simple string and vice versa
str_data = str(quiz)
quiz2 = NagimQuiz.from_string(str_data)

# Very easy lol
```

### NagimQuestion
Class that contains question and operations over it.
```python
from QuizGeneratorModel.quiz_craft_package.containers.nagim_question import NagimQuestion

question = NagimQuestion.from_array(["What is the best programming language?", ["Python", "Rust", "KUMIR", "Scratch", "C++"], ["KUMIR", "Scratch"]])

print(question.question_text) # What is the best programming language?

print(question.options) # ["Python", "Rust", "KUMIR", "Scratch", "C++"]

print(question.right_answers) # ["KUMIR", "Scratch"]

print(question.right_answers_indexes) # [2, 3]

# Very easy lol
```

## Fast documentation table
Please only use the public methods described in this table.
### QuizGenerator
| Method | Description |
| --- | --- |
| `create_quiz_from_files(file_paths: list[str], max_questions: int)` | Return NagimQuiz object generated from files that are specified by file_paths list. You can optionally set maximum number of questions in the quiz. |
| `QuizGenerator(debug: bool)` | Create instance of QuizGenerator. If debug set to true, then it will show generation logs (default is False). |

### QuizDataBase

| Method | Description |
| --- | --- |
| `save_quiz(quiz: NagimQuiz, unique_id: str)` | Save quiz in vector database with unique id. You can search among all saved quizzes. |
| `search_quiz(query: str, number_of_results: int)` | Return 'number_of_results' number of quizzes that are the most suitable for search query 'query'. Return type is list[tuple [NagimQuiz,str]]. Second element of tuple is unique id that you specified during saving.|
| `QuizDataBase(save_folder_path: str)` | Create quiz database instance. It will automaticly save and load quizzes in/from specified folder. So you do not need always re-save quizzes for search. If you want to erase quiz data, just delete content of specified folder (really do not forget to do it or say goodbye to your memory).|

### QuizDescriber

| Method | Description |
| --- | --- |
| `generate_description(quiz: NagimQuiz)` | Generate description for quiz. Return quiz with description. |

### NagimQuiz
Use 'get_question(index)' or iterate through the instance in loop to access questions. Too easy. To get number of question just write 'len(quiz)'.

### NagimQuestion
| Property | Description |
| --- | --- |
| `question_text` | String that contains question sentence. |
| `options` | Answer options (list[str]).|
| `right_answers` | Right answers (list[str]).|
| `right_answers_indexes` | Right answers indexes (list[**int**]).|
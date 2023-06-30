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
from quiz_craft_package.quiz_database import QuizDataBase

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
## Quiz objects
### NagimQuiz
Class that contain quiz questions and operations over it.
```python
from quiz_craft_package.containers.nagim_quiz import NagimQuiz

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
from quiz_craft_package.containers.nagim_question import NagimQuestion

question = NagimQuestion.from_array(["What is the best programming language?", ["Python", "Rust", "KUMIR", "Scratch", "C++"], ["KUMIR", "Scratch"]])

print(quiestion.question_text) # What is the best programming language?

print(quiestion.options) # ["Python", "Rust", "KUMIR", "Scratch", "C++"]

print(quiestion.right_answers) # ["KUMIR", "Scratch"]

print(quiestion.right_answers_indexes) # [2, 3]

# Very easy lol
```

## Fast documentation table
### QuizGenerator
| Method | Description |
| --- | --- |
| `create_quiz_from_files(file_paths: list[str], max_questions: int` | Return NagimQuiz object generated from files that are specified by file_paths list. You can optionally set maximum number of questions in the quiz. |
| `QuizGenerator(debug: bool)` | Create instance of QuizGenerator. If debug set to true, then show generation logs (default is False). |

[yeeeaaahhh!](https://www.youtube.com/watch?v=x98mHJHY-P0)
[puke](https://www.youtube.com/watch?v=gWXzbZUiFwI)
[raaawwwr!](https://www.youtube.com/watch?v=hzaV9BqLSuY)
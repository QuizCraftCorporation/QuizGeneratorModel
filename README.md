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
database = QuizDataBase("./path/to/vector_db_cache_saving")

# Save quizzes in vector database
# quiz is 'NagimQuiz' object!
database.save_quiz(quiz1)
database.save_quiz(quiz2)
database.save_quiz(quiz3)

result = database.search_quiz("German war", number_of_results=3)
# First argument is a search query
# Second is a number of top most similar quizzes to show.
```
## Quiz objects
VERY IMPORTANT!!!
```python
[
    [
        "Question text", 
        ["option 1", "option 2", ...],
        [0] #Indexes of true options
    ],
    [
        "Question text", 
        ["option 1", "option 2", ...],
        [0, 2]
    ],
    ...
]
```
Just python array

### Questions are good. Nothing can be better than ChatGPT

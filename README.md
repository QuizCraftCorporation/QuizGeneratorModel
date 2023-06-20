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
```python
# If you save everything in folder QuizGeneratorModel
# If not then use from folder_name.quiz_generator import QuizGenerator
from QuizGeneratorModel.quiz_craft_package.quiz_generator import QuizGenerator

quiz_gen = QuizGenerator(debug=False)
# Set debug=True if you want to see generation progress logs.

result = quiz_gen.create_questions_from_file(["path/to/text1.txt", "path/to/text2.pdf"])
# Argument is a list of files
# Support .pdf and .txt at this moment.

```

## Quiz format
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

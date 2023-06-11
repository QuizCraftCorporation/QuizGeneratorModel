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
4. Make sure that you have installed **lfs**
```console
git lfs install
```

5. Download models
```console
git clone https://huggingface.co/potsawee/t5-large-generation-squad-QuestionAnswer
```
(Move all files of this repository to **resources/t5MCQ_gen**)

```console
git clone https://huggingface.co/potsawee/t5-large-generation-race-Distractor
```
(Move all files of this repository to **resources/t5MCQ_dis**)
<br/>
Do not include repository root folder!

## How to use
```python
from generate_quiz import generate_quiz

result = generate_quiz("path/to/text.txt", debug=False)
# Set debug=True if you want to see generation progress logs
```

## Quiz format
```python
[
    [
        "Question text", 
        ["option 1", "option 2", ...]
    ],
    [
        "Question text", 
        ["option 1", "option 2", ...]
    ],
    ...
]
```
Just python array
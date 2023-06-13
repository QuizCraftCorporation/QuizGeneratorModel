from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class MCQGenerator:
    def __init__(self) -> None:
        self.create_tokenizer = AutoTokenizer.from_pretrained("./resources/t5MCQ_gen/")
        self.create_model = AutoModelForSeq2SeqLM.from_pretrained("./resources/t5MCQ_gen/")
        self.distract_tokenizer = AutoTokenizer.from_pretrained("./resources/t5MCQ_dis/")
        self.distract_model = AutoModelForSeq2SeqLM.from_pretrained("./resources/t5MCQ_dis/")

    def generate_question(self, text: str):
        inputs = self.create_tokenizer(text, return_tensors="pt")
        outputs = self.create_model.generate(**inputs, max_length=100)
        #Почему 1? Есть несколько вопросов?
        question_answer = self.create_tokenizer.decode(outputs[0], skip_special_tokens=False)
        question_answer = question_answer.replace(self.create_tokenizer.pad_token, "").replace(self.create_tokenizer.eos_token, "")
        question, answer = question_answer.split(self.create_tokenizer.sep_token)
        distractions = self._get_distractions(text, question, answer)
        return [question, distractions + [answer]]

    def _get_distractions(self, context: str, question: str, answer: str):
        input_text = " ".join([question, self.distract_tokenizer.sep_token, answer, self.distract_tokenizer.sep_token, context])
        inputs = self.distract_tokenizer(input_text, return_tensors="pt")
        outputs = self.distract_model.generate(**inputs, max_new_tokens=128)
        distractors = self.distract_tokenizer.decode(outputs[0], skip_special_tokens=False)
        distractors = distractors.replace(self.distract_tokenizer.pad_token, "").replace(self.distract_tokenizer.eos_token, "")
        distractors = [y.strip() for y in distractors.split(self.distract_tokenizer.sep_token)]
        return self._filter_same_distractors(distractors)
    
    def _filter_same_distractors(self, options: list[str]):
        filtered_distractors = []
        for option in options:
            if not option in filtered_distractors:
                filtered_distractors.append(option)
        return filtered_distractors

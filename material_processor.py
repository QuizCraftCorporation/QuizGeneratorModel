from transformers import AutoTokenizer
from langchain.text_splitter import RecursiveCharacterTextSplitter

class MaterialProcessor:
    """
    Class that compress text data for tutorial creation model.
    """

    def __init__(self, path) -> None:
        self._tokenizer = AutoTokenizer.from_pretrained("./question_model/")
        self._text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=20,
            length_function=self._tiktoken_len,
            separators=['\n\n', '\n', ' ', '']
        )
        material_file = open(path, "r", encoding="utf-8")
        compressed_text = self._compress_text(material_file.read())
        material_file.close()
        self._text_data = compressed_text

    def _compress_text(self, text) -> list[str]:
        chunks = self._text_splitter.split_text(text)
        return chunks
    
    def _tiktoken_len(self, text):
        tokens = self._tokenizer(text, return_tensors="pt")
        return tokens.input_ids.shape[1]

    @property
    def text_data(self):
        return self._text_data
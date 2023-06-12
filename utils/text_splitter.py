from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextSplitter:
    """
    Class that compress text data for tutorial creation model.
    """

    def __init__(self, text: str, tokenizer) -> None:
        self._tokenizer = tokenizer
        self._text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=20,
            length_function = self._token_len,
            separators=['\n\n', '\n', ' ', '']
        )
        self._text_chunks = self._text_splitter.split_text(text)
        self._text_chunks = [text_chunk.replace('\n', '') for text_chunk in self._text_chunks]

    def _token_len(self, text: str):
        tokens = self._tokenizer(text, return_tensors="pt")
        return tokens.input_ids.shape[1]

    @property
    def text_chunks(self):
        return self._text_chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextSplitter:
    """
    Class that compress text data for tutorial creation model.
    """

    def __init__(self, tokenizer) -> None:
        self._tokenizer = tokenizer
        self._text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=20,
            length_function = self._token_len,
            separators=['\n\n', '\n', ' ', '']
        )

    def _token_len(self, text: str):
        tokens = self._tokenizer(text, return_tensors="pt")
        return tokens.input_ids.shape[1]

    def split_text(self, text: str):
        text_chunks = self._text_splitter.split_text(text)
        text_chunks = [text_chunk.replace('\n', '') for text_chunk in text_chunks]
        return text_chunks
import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextSplitter:
    """
    Class that compress text data for quiz generation model.
    """

    def __init__(self) -> None:
        self._text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=20,
            length_function = self._token_len,
            separators=['\n\n', '\n', ' ', '']
        )

    def _token_len(self, text: str):
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))

    def split_text(self, text: str):
        text_chunks = self._text_splitter.split_text(text)
        text_chunks = [text_chunk.replace('\n', '') for text_chunk in text_chunks]
        return text_chunks
    
    def cut_by_tokens(self, text: str, number_of_tokens: int):
        enc = tiktoken.get_encoding("cl100k_base")
        encoded = enc.encode(text)
        cutted_text = enc.decode(encoded[:number_of_tokens])
        return cutted_text
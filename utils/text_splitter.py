from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextSplitter:
    """
    Class that compress text data for tutorial creation model.
    """

    def __init__(self, text: str) -> None:
        self._text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1700,
            chunk_overlap=400,
            separators=['\n\n', '\n', ' ', '']
        )
        self._text_chunks = self._text_splitter.split_text(text)
        self._text_chunks = [text_chunk.replace('\n', '') for text_chunk in self._text_chunks]

    @property
    def text_chunks(self):
        return self._text_chunks
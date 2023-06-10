from langchain.document_loaders import PyPDFLoader

class FileReader:
    def __init__(self, filepath) -> None:
        ext = filepath.split('.')[-1]
        if not ext in ['txt', 'pdf']:
            raise Exception(f"Unsupported file format: {ext}")
        if ext == 'txt':
            input_file = open(filepath, "r", encoding="utf-8")
            self._content = input_file.read()
            input_file.close()
        elif ext == 'pdf':
            loader = PyPDFLoader(filepath)
            data = loader.load()
            self._content = ' '.join([page.page_content for page in data])


    def get_content(self) -> str:
        return self._content
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader =DirectoryLoader(
    path='book',
    glob="*.pdf",
    loader_cls=PyPDFLoader
)
doc=loader.load()

print(doc[50].page_content)

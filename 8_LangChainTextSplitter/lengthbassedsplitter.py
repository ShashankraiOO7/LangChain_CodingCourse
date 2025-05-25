from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('Assigment.pdf')

doc=loader.load()

split=CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result=split.split_documents(doc)

print(result[0].page_content)
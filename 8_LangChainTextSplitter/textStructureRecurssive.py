from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader('Assigment.pdf')
doc=loader.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size= 200,
    chunk_overlap=0,
    separators=''
)

result=splitter.split_documents(doc)

print(result[0].page_content)
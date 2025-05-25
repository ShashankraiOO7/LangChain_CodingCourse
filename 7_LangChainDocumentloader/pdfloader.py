from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader('Algorithms to Live By_ The Computer Science of Human Decisions - PDF Room.pdf')
doc= loader.load()

print(doc[15])
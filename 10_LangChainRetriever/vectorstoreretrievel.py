from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

embedingmodel=GoogleGenerativeAIEmbeddings(model="models/embedding-001")

vecterstore=FAISS.from_documents(
    documents=docs,
    embedding=embedingmodel
    
)

retriever=vecterstore.as_retriever(search_kwargs={"k": 2})
query = "What is Chroma used for?"
results = retriever.invoke(query)
print(len(results))
for i in range(0,len(results)):
    print(f"\n--- Result {i+1} ---")
    print(results[i].page_content)
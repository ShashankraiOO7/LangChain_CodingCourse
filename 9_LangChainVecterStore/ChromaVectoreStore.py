from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()

# Initialize embedding function
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Define documents
doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
    metadata={"team": "Royal Challengers Bangalore"}
)
doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
    metadata={"team": "Mumbai Indians"}
)
doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Chennai Super Kings"}
)
doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
    metadata={"team": "Mumbai Indians"}
)
doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
    metadata={"team": "Chennai Super Kings"}
)
docs = [doc1, doc2, doc3, doc4, doc5]

# Initialize Chroma vector store
vector_store = Chroma(
    embedding_function=embedding,
    persist_directory='my-db2',
    collection_name='chromadb'
)

# Add documents to the vector store
vector_store.add_documents(docs)

# View stored documents
print(vector_store.get(include=['embeddings', 'documents', 'metadatas']))

# Perform similarity search
result = vector_store.similarity_search(
    query='Who among these are a bowler?',
    k=2
)
print(result)

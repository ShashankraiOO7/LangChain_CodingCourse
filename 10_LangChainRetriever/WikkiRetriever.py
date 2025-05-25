from langchain_community.retrievers import WikipediaRetriever

retriever=WikipediaRetriever(top_k_results=3,lang='en')

result=retriever.invoke('tell me about IPL')

print(result)
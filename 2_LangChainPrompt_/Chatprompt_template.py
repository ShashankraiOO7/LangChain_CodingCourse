from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()
model =GoogleGenerativeAI(model='gemini-1.5-pro')


chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in simple terms, what is {topic}')
])

domain=input("Enter Domain\t ")
topic=input("Enter Topic\t ")

prompt = chat_template.invoke({'domain':domain,'topic':topic})
print( prompt)
print(model.invoke(prompt))
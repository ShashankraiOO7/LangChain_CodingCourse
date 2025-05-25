from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model =GoogleGenerativeAI(model='gemini-1.5-pro')


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# load chat history
with open('history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(model.invoke(prompt))
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv


load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-pro')
#Using list with Langachain Functionality to store Messages/Maintain Hi

chat_history=[
    SystemMessage(content=input("Enter the area of Expert"))
    ]
while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ',result.content)
print(chat_history)
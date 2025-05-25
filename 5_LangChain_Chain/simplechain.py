from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

template=PromptTemplate(
    template="Tell me about the{topic}\n",
    input_variables=['topic']
)

parser=StrOutputParser()

chain =template | model | parser

print(chain.invoke({'topic':'AI'}))




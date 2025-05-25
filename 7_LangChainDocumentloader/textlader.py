from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import StringPromptTemplate,PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

loader=TextLoader('doc.txt',encoding='utf-8')
doc=loader.load()
model= ChatGoogleGenerativeAI(model='gemini-1.5-pro')

parser= StrOutputParser()
template=PromptTemplate(
    template='Write 6 line poem {text}\n',
    input_variables=['text']
)
chain=template | model | parser

print(chain.invoke({'text':doc}))
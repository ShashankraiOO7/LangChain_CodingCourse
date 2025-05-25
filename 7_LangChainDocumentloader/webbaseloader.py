from langchain_community.document_loaders import SeleniumURLLoader,WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model= ChatGoogleGenerativeAI(model='gemini-1.5-pro')
template = PromptTemplate(
    template='Analysis the text and gave the answer{input}\n',
    input_variables='input'
)

parser=StrOutputParser()

urls=    'https://www.flipkart.com/acer-aspire-3-intel-celeron-dual-core-n4500-8-gb-512-gb-ssd-windows-11-home-a324-45-thin-light-laptop/p/itmbbfe217e40d59'

loader = WebBaseLoader(urls)
doc=loader.load()

chain= template|model|parser

print(chain.invoke({'input':doc}))
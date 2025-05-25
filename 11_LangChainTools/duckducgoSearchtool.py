from langchain_community.tools import DuckDuckGoSearchResults
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

Search_tool =DuckDuckGoSearchResults()

context = Search_tool.invoke("KKR vs CSK match Update")
print("Context_loaded")
template =PromptTemplate(
    template='Generate the 5 pointer form the {context}\n',
    input_variables=['context']
)
print("template")
parser =StrOutputParser()
chain = template|model|parser

output =chain.invoke({'context':context})

print(output)




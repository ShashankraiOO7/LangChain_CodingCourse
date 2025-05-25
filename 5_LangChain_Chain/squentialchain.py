from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

template_1 = PromptTemplate(
    template="Tell me detail about the{topic}\n",
    input_variables=['topic']
)
template_2 = PromptTemplate(
    template="generate me the summery{text}\n",
    input_variables=['text']
)

parser=StrOutputParser()

chain= template_1|model|parser|template_2|model|parser
print(chain.invoke({'topic':'Black-Hole'}))

chain.get_graph().print_ascii()
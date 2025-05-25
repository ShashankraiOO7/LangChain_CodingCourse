from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

template1=PromptTemplate(
    template='Generate the poem on the topic {topic}\n',
    input_variables=['topic']
)
template2=PromptTemplate(
    template='Generate the explaination of the poem {poem}\n',
    input_variables=['poem']
)
parser=StrOutputParser()

chain= RunnableSequence(template1,model,parser,template2,model,parser)

print(chain.invoke({'topic':'AI'}))

chain.get_graph().print_ascii()


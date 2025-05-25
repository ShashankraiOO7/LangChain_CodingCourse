from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

template1=PromptTemplate(
    template='Generate 5 line poem on the topic {topic}\n',
    input_variables=['topic']
)
template2=PromptTemplate(
    template='Generate 3line  explaination of the poem {poem}\n',
    input_variables=['poem']
)
parser=StrOutputParser()

generateChain=RunnableSequence(template1,model,parser)

passthroughChain=RunnableParallel({
    'poem': RunnablePassthrough(),
    'explaination': RunnableSequence(template2,model,parser)
}
)

chain= RunnableSequence(generateChain,passthroughChain)

print(chain.invoke({'topic':'AI'}))
chain.get_graph().print_ascii()
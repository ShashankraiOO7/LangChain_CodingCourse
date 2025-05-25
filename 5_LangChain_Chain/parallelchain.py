from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
template1=PromptTemplate(
    template="Generate the detailed Notes about 6 paragraph on the topic {topic}\n",
    input_variables=['topic']   
)
template2=PromptTemplate(
    template="Generate 10 MCQ on the topic {topic}\n",
    input_variables=['topic']
)
template3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz} ',
    input_variables=['topic','quiz']
)
parsser=StrOutputParser()

Parallel_chain=RunnableParallel({
    'notes':template1|model|parsser,
    'quiz':template2|model|parsser
})
merge_chain=template3|model|parsser

chain= Parallel_chain|merge_chain

print(chain.invoke({'topic':'AI'}))

chain.get_graph().print_ascii()

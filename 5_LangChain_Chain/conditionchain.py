from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field,BaseModel
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

class outputParser(BaseModel):
    sentiment : Literal ['positive','negative'] = Field(description="Sentimate of the feedback")

parser_1= PydanticOutputParser(pydantic_object=outputParser)



template=PromptTemplate(
    template='Classify the given feedback as positive or negative {feedback}\n{format_require}',
    input_variables=['feedback'],
    partial_variables={'format_require':parser_1.get_format_instructions()}
)
classificationChain = template|model|parser_1



template1=PromptTemplate(
    template='Gave 1 the appropriate response to the possitive feedback{feedback}\n',
    input_variables=['feedback']
)
template2=PromptTemplate(
    template='Write the appropriate response to the negative feedback{feedback}\n',
    input_variables=['feedback']
)

parser=StrOutputParser()

conditional_chain=RunnableBranch(
    (lambda x:x.sentiment == 'positive',template1|model|parser),
    (lambda x:x.sentiment == 'negative', template2|model|parser),
    RunnableLambda(lambda x: "No Sentiment found")
    )

chain =classificationChain | conditional_chain

print(chain.invoke({'feedback':"This is very good phone"}))

chain.get_graph().print_ascii()
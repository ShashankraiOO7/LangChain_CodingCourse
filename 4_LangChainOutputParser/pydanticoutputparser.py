from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser,BaseOutputParser
from pydantic import BaseModel,Field

load_dotenv()

# Define the model
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

class struct(BaseModel):
    name:str = Field(description='Name of the Person')
    age: int = Field(gt=18,description="gave me the Age")
    country: str =Field(description='Write the name of the country')
parser= PydanticOutputParser(pydantic_object=struct)

template=PromptTemplate(
    template='Write the name of the man of the country{country} Age of the man and name of the country\n {format} ',
    input_variables=['country'],
    partial_variables={'format':parser.get_format_instructions()}
    
)

chain = template | model | parser

final_result = chain.invoke({'country':'sri lankan'})

print(final_result)
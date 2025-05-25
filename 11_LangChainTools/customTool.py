from langchain.tools import tool

# 1st Way to Make Tools
#Create Function then add type hint after  that add decorator
@tool #<- This is Decorator
def multiply(a:int,b:int)->int:
    '''This tool is for Multiplication'''
    return a*b
result = multiply.invoke({"a":3, "b":5})
print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)

#2nd way to Making tools by the help of StructuredTools
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field

# Define input schema using pydantic
class MultiplyInput(BaseModel):
    a: int = Field(description="This is the first integer value for multiplication")
    b: int = Field(description="This is the second integer value for multiplication")

# Define the actual function
def multiply2(a: int, b: int) -> int:
    return a * b

# Create a StructuredTool
structure_tool = StructuredTool.from_function(
    func=multiply2,
    name="Multiply",
    description="This tool multiplies two integers.",
    args_schema=MultiplyInput
)

# Call the tool using dictionary (StructuredTool expects kwargs)
result = structure_tool.invoke({"a": 4, "b": 5})

# Output
print(result)
print(structure_tool.name)
print(structure_tool.description)
print(structure_tool.args_schema.schema())



#3rd Way to Make Tools   ->   Using BaseTool Class
from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

# arg schema using pydantic

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to add")
    b: int = Field(required=True, description="The second number to add")
    
    
class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two numbers"

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b
multiply_tool = MultiplyTool()

result = multiply_tool.invoke({'a':3, 'b':3})

print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)

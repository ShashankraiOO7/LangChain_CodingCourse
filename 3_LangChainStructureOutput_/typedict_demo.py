from typing import TypedDict

class person(TypedDict):
    name:str
    age: int
   
new_person: person= {'Shashank','34'}


print(new_person)
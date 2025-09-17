# Basic example
# Default values
# Optional fields
# Coerce
# Builtin validation
# Field Function -> default values, constraints, description, regex
# expressions
# Returns pydantic object -> convert to json/dict
from pydantic import BaseModel,EmailStr,Field
from typing import Optional


class Student(BaseModel):
    name:str = 'Rishit'  #default value
    age:Optional[str] = None
    email:EmailStr
    cgpa:float = Field(gt=0, lt=10, default=7, description="A decimal value representing the cgpa of the student") # contraints and description to llm like we have in annotation in typeddict

new_student={'age':'23','email':'rishit@gmail.com'}
student= Student(**new_student)

print(student)
student_dict=dict(student)
print(student_dict)

student_json= student.model_dump_json()
print(student_json)
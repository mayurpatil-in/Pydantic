# TODO: Create Employee model
# Fields:
# - id: int
# - name: str (min 3 chars)
# - department: optional str (default 'General')
# - salary: float (must be >= 10000)

from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id : int
    name : str = Field(
        ...,
        min_length=3,
        max_length=50,
        description= "Employee Name",
        examples="Mayur Patil"
    )
    department : Optional[str] = 'General'
    salary : float = Field(..., ge=10000)

input_data = {'id': 101, 'name': "May", 'department':"General", 'salary': 10000.00}

employee = Employee(**input_data)
print(employee)
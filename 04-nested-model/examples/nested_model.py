from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

address = Address(
    street= "123 something",
    city= "Kolhapur",
    postal_code= "45128"
)

user = User(
    id= 1,
    name= "Mayur",
    address= address
)

comment = Comment(
    id= 1,
    content= "First Comment",
    replies= [
        Comment(id=2, content="reply1"),
        Comment(id=3, content="reply2")
    ]
)
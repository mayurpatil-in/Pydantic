#Todo- Create Product model with id,name,price,in_stock
from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True

input_data = {'id': 101, 'name': "Mayur", 'price': 45.00, 'in_stock': True}

product = Product(**input_data)
print(product)






    
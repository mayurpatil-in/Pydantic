from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    username : str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 Characters")
        return v
    
class SignupData(BaseModel):
    password : str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password do not match')
        return values
    
class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    
# Product
input_data = {'price': 20.00, 'quantity':2}
product = Product(**input_data)
print(product)

# Passsword Match
input_data = {'password': "mayur", 'confirm_password':"mayur"}
signup = SignupData(**input_data)
print(signup)

# Username
input_data = {'username': "Mayur"}
user = User(**input_data)
print(user)
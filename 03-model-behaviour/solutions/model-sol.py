# TODO: Create Booking model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >=1)
# - rate_per_night: float
# Also, add computed field: total_amount = nights * rate_per_night

from pydantic import BaseModel, Field, computed_field

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field (ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
    
input_data = {'user_id': 101, 'room_id': 2, 'nights':2, 'rate_per_night':200}
booking = Booking(**input_data)
print(booking)

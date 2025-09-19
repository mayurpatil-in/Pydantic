from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id : int
    items : List[str]
    quantities : Dict[str, int]

class BlodPost(BaseModel):
    title : str
    content : str
    img_url : Optional[str] = None

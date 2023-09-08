from pydantic import BaseModel

# 2. Class which Message Details
class Message(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float
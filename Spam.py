from pydantic import BaseModel

# 2. Class which Message Details
class Spam(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float
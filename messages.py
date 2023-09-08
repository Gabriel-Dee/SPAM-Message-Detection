from pydantic import BaseModel

# 2. Class which Message Details
class Message(BaseModel):
    message: str
    length: int
    punct: int
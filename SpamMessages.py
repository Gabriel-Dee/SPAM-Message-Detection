from pydantic import BaseModel

# 2. Class which Message Details
class SpamMessage(BaseModel):
    message: str
    length: int
    punct: int
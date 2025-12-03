from pydantic import BaseModel

class MoodRequest(BaseModel):
    mood: str

class MoodResponse(BaseModel):
    message: str

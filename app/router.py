from fastapi import APIRouter
from app.schemas import MoodRequest, MoodResponse
from app.mood_responses import mood_to_message

router = APIRouter()

@router.post("/mood", response_model=MoodResponse)
def get_mood_message(req: MoodRequest):
    mood = req.mood
    message = mood_to_message.get(mood, "無論如何，你都值得被好好對待 ❤️")
    return {"message": message}

from fastapi import APIRouter
from app.mood_responses import generate_mood_reply
from app.schemas import MoodRequest, MoodResponse

router = APIRouter()

@router.post("/mood", response_model=MoodResponse)
def mood_api(req: MoodRequest):
    return {"reply": generate_mood_reply(req.mood)}

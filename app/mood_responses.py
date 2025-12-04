def generate_mood_reply(mood: str) -> str:
    mood = mood.lower()
    if "sad" in mood or "難過" in mood:
        return "我懂你的感受，你已經做得很好了。"
    if "happy" in mood or "開心" in mood:
        return "太好了！保持這份好心情！"
    return "無論什麼心情，我都在這裡支持你。"

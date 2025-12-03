from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router

app = FastAPI(
    title="Mood Diary API",
    description="輸入心情，回傳一句鼓勵的 FastAPI 專案",
    version="1.0"
)

# ⭐ 允許前端連線（很重要）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 若你之後部署，可以換成你的 domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Mood Diary API is running!"}


# Serve frontend static files (optional)
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

frontend_dir = Path(__file__).resolve().parents[1] / "frontend"
# mount static files at /static
if frontend_dir.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_dir)), name="static")

    @app.get("/app", include_in_schema=False)
    def serve_frontend():
        index = frontend_dir / "index.html"
        if index.exists():
            return FileResponse(str(index))
        return {"detail": "frontend not found"}

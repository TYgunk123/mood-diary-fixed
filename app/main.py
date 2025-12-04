from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.router import router

app = FastAPI(
    title="Mood Diary API",
    description="輸入心情，回傳一句鼓勵的 FastAPI 專案",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def root():
    return {"status": "ok"}

# Serve frontend (root-level frontend directory)
frontend_dir = Path(__file__).resolve().parents[1] / "frontend"
if frontend_dir.exists():
    # mount static files at /static
    app.mount("/static", StaticFiles(directory=str(frontend_dir)), name="static")

    @app.get("/app", include_in_schema=False)
    def serve_frontend():
        index = frontend_dir / "index.html"
        if index.exists():
            return FileResponse(str(index))
        return {"detail": "frontend not found"}

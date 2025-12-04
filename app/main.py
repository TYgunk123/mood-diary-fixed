from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.router import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def root():
    return {"status": "ok"}

frontend_dir = Path(__file__).resolve().parents[1] / "frontend"
if frontend_dir.exists():
    @app.get("/app", include_in_schema=False)
    def serve_frontend():
        index = frontend_dir / "index.html"
        if index.exists():
            return FileResponse(str(index))
        return {"error": "no index"}

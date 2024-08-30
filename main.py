from fastapi import FastAPI, responses
import uvicorn
from app.api.routers import router as api_router
import os
from dotenv import load_dotenv
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

env_path = Path(".") / ".env"
load_dotenv(env_path)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def redirigir_a_docs():
    return responses.RedirectResponse(url="/docs")


app.include_router(api_router, prefix="/api")
if os.getenv("VER_DBS") in ["True", "1"]:

    print("-" * 70)
    print("Bases de datos Conectadas".center(70, " "))
    print()
    for db_title, db_url in settings.URL_DBs.items():
        print(db_title.center(70, " "))
        print()
        print(db_url.center(70, " "))
        print("-" * 70)

    print()
HOST_IP = (
    os.getenv("SERVER_HOST") or "127.0.0.1"
)  # si encuentra la ip en el .env, lo usa sino por defecto localhost

PORT = (
    int(os.getenv("SERVER_PORT")) or 3002  # type: ignore
)  # si encuentra el port en el .env, lo usa sino por defecto 3002
if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, reload=True, log_level="info", host=HOST_IP)

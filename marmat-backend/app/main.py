from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.common.response import success

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:2057"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

@app.get("/api/health")
def heath_status():
    return success(data="API Status Healthy")

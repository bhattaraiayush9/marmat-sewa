from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:2729'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

@app.get("/api/")
async def root():
    return {"message": "This is the thing from the thing."}


@app.get("/route")
async def route():
    return {"status": 200, "message": "Hello, this is the /route", "data": []}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

tasks: list[str] = []

frontend_url = "http://localhost:3000"
origins = [
    frontend_url,
]

# https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/messages")
async def get_message() -> list[str]:
    return tasks

@app.get("/addmessage")
async def addmessage(message: str) -> str:
    tasks.append(message)
    return "success"
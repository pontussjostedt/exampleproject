from fastapi import FastAPI

app = FastAPI()

tasks: list[str] = []

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
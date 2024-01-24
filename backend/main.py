from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/messages")
async def get_message() -> list[str]:
    return ["Bob", "Foo", "Bar"]
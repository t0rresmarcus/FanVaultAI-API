from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/Sara")
async def root():
    return {"message": "Hello World, Sara"}
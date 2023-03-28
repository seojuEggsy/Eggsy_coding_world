from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/")
async def create_item(item: str):
    print(item)
    return {"item": item}

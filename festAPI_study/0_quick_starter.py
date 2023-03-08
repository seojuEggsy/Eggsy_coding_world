from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_query_param(message: str):
    return {"message": message}

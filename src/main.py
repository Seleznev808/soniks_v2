from fastapi import FastAPI

app = FastAPI(title="soniks_v2")


@app.get("/", description="hello")
async def root():
    return {"message": "Hello soniks_v2"}

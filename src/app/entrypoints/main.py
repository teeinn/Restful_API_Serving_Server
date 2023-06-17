from fastapi import FastAPI
from app.entrypoints import controller

app = FastAPI()
app.include_router(controller.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Inference Server"}



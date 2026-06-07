from fastapi import FastAPI

app = FastAPI(title="TaskFlow")

@app.get("/")
def home():
    return {"message": "TaskFlow"}

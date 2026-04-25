from fastapi import FastAPI
app = FastAPI(title="Test")

@app.get("/")
def read_root():
    return {"message": "Welcome to Test API"}

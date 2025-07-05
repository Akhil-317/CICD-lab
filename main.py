from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Welcome to Jenkins, CI/CD pipeline"}

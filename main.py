from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}
@app.get("/about")
def about():
    return {"info": "This is a simple FastAPi example"}

@app.get("/student/{name}")
def get_student(name: str):
    return {"student_name": name}
@app.post("/square/{number}")
def square(number: int):
    return {"number": number,"square": number*number}
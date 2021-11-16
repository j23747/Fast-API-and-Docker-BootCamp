from fastapi import FastAPI, Form 
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return { "Lux app": "Welcome to Lux app" } 



@app.get("/about-us")

def read_about_us():
    return { "Lux app": "About us" }

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}    
 
if __name__ == "__main__":
    uvicorn.run('server:app', port=8000, reload=False)
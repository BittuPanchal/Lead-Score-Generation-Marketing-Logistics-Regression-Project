from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory database to store names and email addresses
fake_db = {
    "Alice": "alice@example.com",
    "Bob": "bob@example.com",
    "Charlie": "charlie@example.com"
}

class NameRequest(BaseModel):
    name: str

class EmailResponse(BaseModel):
    email: str

@app.post("/get_email/", response_model=EmailResponse)
def get_email(request: NameRequest):
    name = request.name
    if name in fake_db:
        return EmailResponse(email=fake_db[name])
    else:
        raise HTTPException(status_code=404, detail="Name not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)

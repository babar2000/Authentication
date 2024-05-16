from fastapi import FastAPI
from jose import jwt, JWTError # type: ignore
from datetime import datetime, timedelta

ALGORITHM: str = "HS256"
SECRET_KEY: str = "A Very Secure Secret Key"

def create_access_token(subject: str , expires_delta: timedelta) -> str:
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


app: FastAPI = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get-token")
def get_token(name: str):
    access_token_expiry_minutes = timedelta(minutes=15)
    print("access_token_expiry_minutes", access_token_expiry_minutes) 
    generated_token = create_access_token(subject=name, expires_delta=access_token_expiry_minutes)
    return {"access_token": generated_token}

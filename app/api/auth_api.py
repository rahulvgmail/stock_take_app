# app/api/auth_api.py
from fastapi import APIRouter, HTTPException, Depends, Form
from app.services.auth_service import authenticate_user, create_access_token
from datetime import timedelta

router = APIRouter()

@router.post("/token")
def login(email: str = Form(...), password: str = Form(...)):
    user = authenticate_user(email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"user_id": user['user_id']}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

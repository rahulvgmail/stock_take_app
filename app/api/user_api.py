# app/api/user_api.py
from fastapi import APIRouter, HTTPException, Depends, Body
from app.services.user_service import change_user_role, get_user_by_id
from app.security.token import verify_token
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

@router.post("/users/{user_id}/role")
def update_user_role(user_id: int, new_role: str = Body(...), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # Verify the token and extract user data
    payload = verify_token(token, credentials_exception)
    if 'role' not in payload or payload['role'] != 'Admin':
        raise HTTPException(status_code=403, detail="Insufficient permissions")

    # Proceed with changing the user role
    success = change_user_role(user_id, new_role)
    if not success:
        raise HTTPException(status_code=404, detail="User not found or update failed")
    return {"message": "User role updated successfully"}

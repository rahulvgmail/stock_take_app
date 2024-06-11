# app/services/auth_service.py
from app.models import queries, __execute_sql as db
from app.security.passwords import hash_password, verify_password
from app.security.token import create_access_token
from datetime import timedelta

def authenticate_user(email: str, password: str):
    user = db.execute_query(queries.get_user_by_email(), (email,))
    if user and verify_password(password, user['password_hash']):
        access_token = create_access_token(data={"user_id": user.user_id, "role": user.role})
        return access_token
    return None


def create_user(email: str, password: str):
    hashed_password = hash_password(password)
    db.execute_query(queries.create_user(), (email, hashed_password), commit=True)

def get_user_by_email(email: str):
    return db.execute_query(queries.get_user_by_email(), (email,))

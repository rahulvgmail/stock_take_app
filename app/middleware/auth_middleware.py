# app/middleware/auth_middleware.py
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.security.token import verify_token

class AuthMiddleware:
    def __init__(self, app):
        self.app = app
        self.auth_scheme = HTTPBearer()

    async def __call__(self, request: Request, call_next):
        credentials: HTTPAuthorizationCredentials = await self.auth_scheme(request)
        if credentials:
            try:
                payload = verify_token(credentials.credentials, credentials_exception=HTTPException(status_code=401, detail="Could not validate credentials"))
                request.state.user = payload
            except HTTPException:
                raise HTTPException(status_code=401, detail="Invalid authentication")
        return await call_next(request)

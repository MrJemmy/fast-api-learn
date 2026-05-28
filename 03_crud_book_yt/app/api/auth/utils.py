import jwt
import secrets

from datetime import datetime, timedelta, timezone
from app.core.config import settings
from passlib.context import CryptContext
from cryptography.hazmat.primitives import serialization

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Load keys once
private_key = serialization.load_pem_private_key(settings.PRIVATE_KEY.encode(), password=None)
public_key = serialization.load_pem_public_key(settings.PUBLIC_KEY.encode())

def hash_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)

def generate_access_token(user_id: int) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": user_id,
        "iat": now,
        "exp": now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        "type": "access"
    }
    return jwt.encode(payload, private_key, algorithm=settings.JWT_ALGORITHM)

def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token, public_key, algorithms=[settings.JWT_ALGORITHM],
            options={"require": ["exp", "sub", "type"]}
        )
        if payload["type"] != "access":
            raise jwt.InvalidTokenError("Not an access token")
        return payload
    except jwt.ExpiredSignatureError:
        raise
    except jwt.InvalidTokenError:
        raise

def generate_refresh_token()-> str:
    return secrets.token_urlsafe(64)

def hash_token(token: str) -> str:
    return password_context.hash(token)   # bcrypt hash for storage

def verify_token_hash(token: str, hashed: str) -> bool:
    return password_context.verify(token, hashed)
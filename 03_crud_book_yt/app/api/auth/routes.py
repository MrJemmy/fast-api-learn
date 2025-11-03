from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.config import get_session
from app.api.auth.schemas import UserRegisterSchema, UserLoginSchema
from app.api.auth.services import AuthService

router = APIRouter()
auth_service = AuthService()


@router.post("/register")
async def register_user(
        user_data: UserRegisterSchema,
        session: AsyncSession = Depends(get_session)
):
    if auth_service.username_exists(user_data.username, session):
        return None
    if auth_service.email_exists(user_data.email, session):
        return None
    user = await auth_service.register_user(user_data, session)
    return {"message": "User registered successfully", "user": user}


@router.post("/login")
async def login_user(
        login_data: UserLoginSchema,
        session: AsyncSession = Depends(get_session)
):
    user = await auth_service.login_user(
        login_data.identifier, login_data.password, session)
    return {"message": "User logged in successfully", "user": user}


@router.post("/logout")
def logout_user():
    return {"message": "User logged out successfully"}


@router.post("/refresh_token")
def refresh_token():
    return {"message": "Token refreshed successfully"}


@router.post("/forgot_password")
def forgot_password():
    return {"message": "Password reset link sent"}


@router.post("/reset_password")
def reset_password():
    return {"message": "Password reset successfully"}


@router.get("/verify_email")
def verify_email():
    return {"message": "Email verified successfully"}


@router.post("/resend_verification")
def resend_verification():
    return {"message": "Verification email resent"}


@router.post("/change_password")
def change_password():
    # this route must only access by admin users
    return {"message": "Password changed successfully"}

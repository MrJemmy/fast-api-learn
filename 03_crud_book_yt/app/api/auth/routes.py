from fastapi import APIRouter
from app.api.auth.schemas import UserRegisterSchema

router = APIRouter()

@router.post("/register")
def register_user(user_data: UserRegisterSchema):
    return {"message": "User registered successfully"}

@router.post("/login")
def login_user():
    return {"message": "User logged in successfully"}

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
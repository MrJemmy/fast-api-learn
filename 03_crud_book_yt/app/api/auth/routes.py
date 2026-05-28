from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.auth.utils import generate_access_token, decode_access_token, generate_refresh_token, hash_token
from app.db.config import get_session

from app.api.user.model import User
from app.api.auth.schemas import UserRegisterSchema, UserLoginSchema
from app.api.auth.services import AuthService

router = APIRouter()
auth_service = AuthService()


@router.post("/register",
             response_model=User,
             status_code=status.HTTP_200_OK)
async def register_user(
        user_data: UserRegisterSchema,
        session: AsyncSession = Depends(get_session)
):
    try:
        if auth_service.username_exists(user_data.username, session):
            return None
        if auth_service.email_exists(user_data.email, session):
            return None
        user = await auth_service.register_user(user_data, session)
        return user
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection failed : {str(e)}"
        )
    except  Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Something went wrong, please try again later: {str(e)}"
        )


@router.post("/login",
             response_model=User,
             status_code=status.HTTP_200_OK)
async def login_user(
        login_data: UserLoginSchema,
        session: AsyncSession = Depends(get_session)
):
    try:
        if login_data.identifier is None or login_data.password is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid login data"
            )

        if "@" in login_data.identifier:
            user = await auth_service.email_login(
                login_data.identifier, login_data.password, session)
        else:
            user = await auth_service.username_login(
                login_data.identifier, login_data.password, session)

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        access_token = generate_access_token(user.id)
        refresh_token = generate_refresh_token()
        refresh_hash = hash_token(refresh_token)

        return user
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection failed : {str(e)}"
        )
    except  Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Something went wrong, please try again later: {str(e)}"
        )


@router.post("/logout", status_code=status.HTTP_200_OK)
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

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.config import get_session

from app.api.user.services import UserService
from app.api.user.model import User


router = APIRouter()
userService = UserService()


@router.get(
    "/get_all",
    response_model=List[User],
    status_code=status.HTTP_200_OK
)
async def get_users(session: AsyncSession = Depends(get_session)):
    try:
        users = await userService.get_users(session)
        return users
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


@router.get(
    "/get_one",
    response_model=User,
    status_code=status.HTTP_200_OK)
async def get_user(
        user_id: int,
        session: AsyncSession = Depends(get_session),
):
    try:
        users = await userService.get_user_by_id(user_id, session)
        return users
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


@router.get(
        "/update",
            response_model=User,
            status_code=status.HTTP_200_OK)
def update_user():
    try:
        return {"message": "User details"}
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


@router.get("/delete",
            response_model=User,
            status_code=status.HTTP_200_OK)
def delete_user():
    try:
        return {"message": "User details"}
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

# @router.get("/profile")
# def get_profile():
#     return {"message": "User profile"}

# @router.post("/profile/update")
# def update_profile():
#     return {"message": "User profile updated"}

# @router.post("/profile/upload-avatar")
# def upload_avatar():
#     return {"message": "User avatar uploaded"}

# @router.post("/profile/remove-avatar")
# def remove_avatar():
#     return {"message": "User avatar removed"}

# @router.get("/settings")
# def get_settings():
#     return {"message": "User settings"}

# @router.post("/settings/update")
# def update_settings():
#     return {"message": "User settings updated"}

# @router.get("/notifications")
# def get_notifications():
#     return {"message": "User notifications"}

# @router.post("/notifications/mark-as-read")
# def mark_notifications_as_read():
#     return {"message": "Notifications marked as read"}

# @router.post("/notifications/clear")
# def clear_notifications():
#     return {"message": "Notifications cleared"}

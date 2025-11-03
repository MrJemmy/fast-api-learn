from fastapi import APIRouter

router = APIRouter()

@router.get("/get_all")
def get_users():
    return {"message": "Users list"}

@router.get("/get_one")
def get_user():
    return {"message": "User details"}

@router.get("/update")
def update_user():
    return {"message": "User details"}

@router.get("/delete")
def delete_user():
    return {"message": "User details"}

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



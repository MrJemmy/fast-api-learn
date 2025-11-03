from pydantic import BaseModel, Field, EmailStr, field_validator
import re


class UserLoginSchema(BaseModel):
    identifier: str
    password: str


class UserRegisterSchema(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern="^[a-zA-Z0-9_]+$",
        description=(
            "Username must be between 8 and 128 characters long.")
    )
    email: EmailStr
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="Password must be between 8 and 128 characters long."
    )

    @field_validator("password")
    def validate_password(cls, value):
        """
        Custom password validation:
        - At least 1 uppercase letter
        - At least 1 lowercase letter
        - At least 1 number
        - At least 1 special character
        """
        password_regex = re.compile(
            (
                r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)"
                r"(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$"
            )
        )
        if not password_regex.match(value):
            raise ValueError(
                "Password must include at least one uppercase letter, one "
                "lowercase letter, one number, and one special character."
            )
        return value

    @field_validator("username")
    def validate_username(cls, value):
        if not re.match(r"^[a-zA-Z0-9_]+$", value):
            raise ValueError(
                "Username can only contain letters, numbers, and underscores.")
        return value

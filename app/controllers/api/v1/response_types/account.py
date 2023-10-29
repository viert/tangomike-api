from typing import Literal, Optional
from datetime import datetime
from pydantic import BaseModel, root_validator, ValidationError
from . import ObjectIdStr


class AccountMeResponse(BaseModel):
    id: Optional[ObjectIdStr]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    ext_id: Optional[str]
    avatar_url: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class SignupRequest(BaseModel):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: str
    password: str
    password_confirm: str

    @root_validator()
    def validate_password(cls, values):
        if values.get("password_confirm") != values.get("password"):
            raise ValueError(["passwords don't match"])
        return values


class LogoutResponse(BaseModel):
    detail: Literal["logged out"] = "logged out"


class AuthenticationRequest(BaseModel):
    username: str
    password: str

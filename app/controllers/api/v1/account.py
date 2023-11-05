from fastapi import APIRouter, Depends, Body
from croydon.errors import AuthenticationError, BadRequest
from app.extractors import authenticated_user, current_session
from app.models import User, Session
from .response_types.account import (
    AccountMeResponse,
    LogoutResponse,
    AuthenticationRequest,
    SignupRequest,
)

account_ctrl = APIRouter(prefix="/api/v1/account")


@account_ctrl.get("/me")
async def me(user: User = Depends(authenticated_user())) -> AccountMeResponse:
    return AccountMeResponse(**user.to_dict())


@account_ctrl.post("/signup")
async def signup(body: SignupRequest = Body()) -> AccountMeResponse:
    password = body.password
    attrs = body.dict(exclude={"password", "password_confirm"})
    user = User.create(**attrs)
    user.set_password(password)
    await user.save()
    return AccountMeResponse(**user.to_dict())


@account_ctrl.post("/authenticate")
async def authenticate(
        auth_request: AuthenticationRequest = Body(),
        session: Session = Depends(current_session)) -> AccountMeResponse:

    user = await session.user()
    if user:
        raise BadRequest("already authenticated")

    user = await User.get(auth_request.username)
    if user is None or not user.check_password(auth_request.password):
        raise AuthenticationError("invalid username or password")
    session.user_id = user.id

    return AccountMeResponse(**user.to_dict())


@account_ctrl.post("/logout")
async def logout(session: Session = Depends(current_session)) -> LogoutResponse:
    session.user_id = None
    return LogoutResponse(detail="logged out")

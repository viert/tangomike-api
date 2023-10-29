from typing import Optional, Dict, Any
from fastapi.testclient import TestClient
from httpx import Response

from app import app
from app.models import User, Token

from .mongo_mock_test import MongoMockTest


class ApiTest(MongoMockTest):

    client: TestClient

    user: User = None
    user_password: str = "user_password"

    superuser: User = None
    superuser_password: str = "admin"

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        await User.destroy_all()

        self.user = User.create(
            username="test_user",
            email="test_user@example.com",
        )
        self.user.set_password(self.user_password)
        await self.user.save()

        # reset the client to ensure all side effects e.g. cookies from
        # previous tests go away
        self.client = TestClient(app)

    async def request(self,
                      method: str,
                      path: str,
                      data: Optional[Dict[str, Any]] = None,
                      auth: bool = True,
                      token: Optional[Token] = None,
                      user: Optional[User] = None) -> Response:
        headers = {}
        if auth:
            if token is None:
                if user is None:
                    user = self.user
                token = await user.get_valid_token()
            headers["Authorization"] = f"Token {token.token}"
        return self.client.request(method, path, headers=headers, json=data)

    async def get(self,
                  path: str,
                  data: Optional[Dict[str, Any]] = None,
                  auth: bool = True,
                  token: Optional[Token] = None,
                  user: Optional[User] = None) -> Response:
        return await self.request("GET", path, data, auth, token, user)

    async def post(self,
                   path: str,
                   data: Optional[Dict[str, Any]] = None,
                   auth: bool = True,
                   token: Optional[Token] = None,
                   user: Optional[User] = None) -> Response:
        return await self.request("POST", path, data, auth, token, user)

    async def patch(self,
                    path: str,
                    data: Optional[Dict[str, Any]] = None,
                    auth: bool = True,
                    token: Optional[Token] = None,
                    user: Optional[User] = None) -> Response:
        return await self.request("PATCH", path, data, auth, token, user)

    async def put(self,
                  path: str,
                  data: Optional[Dict[str, Any]] = None,
                  auth: bool = True,
                  token: Optional[Token] = None,
                  user: Optional[User] = None) -> Response:
        return await self.request("PUT", path, data, auth, user)

    async def delete(self,
                     path: str,
                     data: Optional[Dict[str, Any]] = None,
                     auth: bool = True,
                     token: Optional[Token] = None,
                     user: Optional[User] = None) -> Response:
        return await self.request("DELETE", path, data, auth, token, user)

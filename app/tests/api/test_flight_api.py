from typing import Optional
from app.tests.api_test import ApiTest
from app.models import User, Flight


class TestFlightApi(ApiTest):

    another_user: Optional[User] = None

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        self.another_user = User.create(username="another_user", email="another@example.com")
        await self.another_user.save()

    async def asyncTearDown(self):
        await Flight.destroy_all()
        if self.another_user:
            await self.another_user.destroy()
            self.another_user = None

    async def test_create_and_check(self):
        resp = await self.post("/api/v1/flights/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        flight_id = data["flight_id"]

        resp = await self.get(f"/api/v1/flights/{flight_id}/check")
        self.assertEqual(resp.status_code, 200)

        resp = await self.get(f"/api/v1/flights/{flight_id}/check", user=self.another_user)
        self.assertEqual(resp.status_code, 404)

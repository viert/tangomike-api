from fastapi import APIRouter, Depends
from croydon.errors import NotFound
from app.extractors import authenticated_user
from app.models import User, Flight
from .response_types.flights import FlightResponse

flights_ctrl = APIRouter(prefix="/api/v1/flights")


@flights_ctrl.post("/")
async def create(user: User = Depends(authenticated_user())) -> FlightResponse:
    flight = Flight.create(user_id=user.id)
    await flight.save()
    return FlightResponse(**flight.to_dict())


@flights_ctrl.get("/{flight_id}/check")
async def check(flight_id: str, user: User = Depends(authenticated_user())) -> FlightResponse:
    flight = await Flight.find_one({"flight_id": flight_id})
    if flight is None or flight.user_id != user.id:
        raise NotFound("flight not found")
    return FlightResponse(**flight.to_dict())

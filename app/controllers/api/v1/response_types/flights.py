from pydantic import BaseModel, validator
from typing import Optional


class FlightResponse(BaseModel):
    id: Optional[str]
    flight_id: Optional[str]
    user_id: Optional[str]

    @validator("id", "user_id", pre=True)
    def convert_ids(cls, v):
        v = str(v)
        return v

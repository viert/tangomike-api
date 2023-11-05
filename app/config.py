from pydantic import BaseModel, Field
from croydon.config import BaseConfig


class GrpcConfig(BaseModel):
    socket: str = "localhost:12000"


# Config class name must not be changed as the bootstrap procedure counts on it
class Config(BaseConfig):
    grpc: GrpcConfig = Field(default_factory=GrpcConfig)

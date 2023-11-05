import grpc
from typing import Optional
from croydon import ctx
from .tangomike_pb2_grpc import TrackStub


def get_new_stub(sock: Optional[str] = None) -> TrackStub:
    if sock is None:
        sock = ctx.cfg.grpc.socket
    chan = grpc.aio.insecure_channel(sock)
    return TrackStub(chan)

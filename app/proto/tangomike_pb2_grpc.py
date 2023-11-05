# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import app.proto.tangomike_pb2 as tangomike__pb2


class TrackStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadTrackStream = channel.stream_stream(
                '/tangomike.Track/UploadTrackStream',
                request_serializer=tangomike__pb2.UploadTrackStreamRequest.SerializeToString,
                response_deserializer=tangomike__pb2.UploadTrackStreamResponse.FromString,
                )
        self.DownloadTrackStream = channel.unary_stream(
                '/tangomike.Track/DownloadTrackStream',
                request_serializer=tangomike__pb2.DownloadTrackStreamRequest.SerializeToString,
                response_deserializer=tangomike__pb2.TrackMessage.FromString,
                )
        self.GetTrack = channel.unary_unary(
                '/tangomike.Track/GetTrack',
                request_serializer=tangomike__pb2.TrackRequest.SerializeToString,
                response_deserializer=tangomike__pb2.TrackResponse.FromString,
                )
        self.GetActiveFlights = channel.unary_unary(
                '/tangomike.Track/GetActiveFlights',
                request_serializer=tangomike__pb2.NoParams.SerializeToString,
                response_deserializer=tangomike__pb2.ActiveFlightsResponse.FromString,
                )


class TrackServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadTrackStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadTrackStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrack(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActiveFlights(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrackServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadTrackStream': grpc.stream_stream_rpc_method_handler(
                    servicer.UploadTrackStream,
                    request_deserializer=tangomike__pb2.UploadTrackStreamRequest.FromString,
                    response_serializer=tangomike__pb2.UploadTrackStreamResponse.SerializeToString,
            ),
            'DownloadTrackStream': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadTrackStream,
                    request_deserializer=tangomike__pb2.DownloadTrackStreamRequest.FromString,
                    response_serializer=tangomike__pb2.TrackMessage.SerializeToString,
            ),
            'GetTrack': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrack,
                    request_deserializer=tangomike__pb2.TrackRequest.FromString,
                    response_serializer=tangomike__pb2.TrackResponse.SerializeToString,
            ),
            'GetActiveFlights': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActiveFlights,
                    request_deserializer=tangomike__pb2.NoParams.FromString,
                    response_serializer=tangomike__pb2.ActiveFlightsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tangomike.Track', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Track(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadTrackStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/tangomike.Track/UploadTrackStream',
            tangomike__pb2.UploadTrackStreamRequest.SerializeToString,
            tangomike__pb2.UploadTrackStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadTrackStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/tangomike.Track/DownloadTrackStream',
            tangomike__pb2.DownloadTrackStreamRequest.SerializeToString,
            tangomike__pb2.TrackMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tangomike.Track/GetTrack',
            tangomike__pb2.TrackRequest.SerializeToString,
            tangomike__pb2.TrackResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetActiveFlights(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tangomike.Track/GetActiveFlights',
            tangomike__pb2.NoParams.SerializeToString,
            tangomike__pb2.ActiveFlightsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

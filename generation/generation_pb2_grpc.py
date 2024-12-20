# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import generation_pb2 as generation__pb2


class GenerationServiceStub(object):
    """
    gRPC services

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Generate = channel.unary_stream(
                '/gooseai.GenerationService/Generate',
                request_serializer=generation__pb2.Request.SerializeToString,
                response_deserializer=generation__pb2.Answer.FromString,
                )
        self.ChainGenerate = channel.unary_stream(
                '/gooseai.GenerationService/ChainGenerate',
                request_serializer=generation__pb2.ChainRequest.SerializeToString,
                response_deserializer=generation__pb2.Answer.FromString,
                )


class GenerationServiceServicer(object):
    """
    gRPC services

    """

    def Generate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChainGenerate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GenerationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Generate': grpc.unary_stream_rpc_method_handler(
                    servicer.Generate,
                    request_deserializer=generation__pb2.Request.FromString,
                    response_serializer=generation__pb2.Answer.SerializeToString,
            ),
            'ChainGenerate': grpc.unary_stream_rpc_method_handler(
                    servicer.ChainGenerate,
                    request_deserializer=generation__pb2.ChainRequest.FromString,
                    response_serializer=generation__pb2.Answer.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gooseai.GenerationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GenerationService(object):
    """
    gRPC services

    """

    @staticmethod
    def Generate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gooseai.GenerationService/Generate',
            generation__pb2.Request.SerializeToString,
            generation__pb2.Answer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChainGenerate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gooseai.GenerationService/ChainGenerate',
            generation__pb2.ChainRequest.SerializeToString,
            generation__pb2.Answer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
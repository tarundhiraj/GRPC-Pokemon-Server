# app.py
import grpc

from concurrent import futures
from .generated import pokemon_pb2_grpc
from .grpc import PokemonServer


class Server:

    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        pokemon_pb2_grpc.add_PokemonServicer_to_server(PokemonServer(), server)
        server.add_insecure_port('[::]:50051')
        print('Starting Server on localhost:50051')
        server.start()
        print('Started Server intance on localhost:50051')
        server.wait_for_termination()

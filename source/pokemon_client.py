import logging
import grpc

from .generated import pokemon_pb2
from .generated import pokemon_pb2_grpc

def convert_pokemon_to_str(pokemon):
    return "Pokemon( Name={0}, Species={1} )" \
            .format(pokemon.p_name,
                    pokemon.p_species
                   )

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pokemon_pb2_grpc.PokemonStub(channel)
        response = stub.getPokemon(pokemon_pb2.PokemonRequest(p_number=1))
    print("Pokemon client received: " + convert_pokemon_to_str(response))


if __name__ == '__main__':
    logging.basicConfig()
    run()

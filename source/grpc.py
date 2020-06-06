import json

from .generated import pokemon_pb2, pokemon_pb2_grpc

JSON_FILE_PATH = "./source/resources/pokemon_db.json"
TAG = "pokemons"


def load_db(filePath=JSON_FILE_PATH):
    pokemon_db = {}
    with open(filePath) as f:
        pokemon_db = json.load(f)
    return pokemon_db.get(TAG, {})


class PokemonServer(pokemon_pb2_grpc.PokemonServicer):
    
    def __init__(self):
        self.pokemons = load_db(JSON_FILE_PATH)

    def getPokemon(self, request, context):
        poke_details = self.pokemons.get(str(request.p_number), {})
        return pokemon_pb2.PokemonResponse(p_number=poke_details.get("number", 0),
                                           p_name=poke_details.get("name", "None"),
                                           p_species=poke_details.get("species", "None"))

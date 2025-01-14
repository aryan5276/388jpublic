import requests


class PokeClient(object):
    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers.update({'User Agent': 'CMSC388J Spring 2024 Project 2'})
        self.base_url = 'https://pokeapi.co/api/v2'

    def get_pokemon_list(self):
        """
        Returns a list of pokemon names
        """
        pokemon = []
        resp = self.sess.get(f'{self.base_url}/pokemon?limit=1200')
        for poke_dict in resp.json()['results']:
            pokemon.append(poke_dict['name'])
        return pokemon
    
    def get_pokemon_ids(self):
        """
        Returns a list of pokemon ids
        """
        ids = []
        resp = self.sess.get(f'{self.base_url}/pokemon?limit=1200')
        for poke_dict in resp.json()['results']:
            tmp = poke_dict['url']
            tmp = tmp[34:]
            curr_id = tmp[:-1]
            ids.append(curr_id)
        return ids
    
    def get_pokemon_info(self, pokemon):
        """
        Arguments:

        pokemon -- a lowercase string identifying the pokemon

        Returns a dict with info about the Pokemon with the 
        following keys and the type of value they map to:
        
        name      -> string
        height    -> int
        weight    -> int
        base_exp  -> int
        moves     -> list of strings
        abilities -> list of strings
        """

        req = f'pokemon/{pokemon}'
        resp = self.sess.get(f'{self.base_url}/{req}')

        code = resp.status_code
        if code != 200:
            raise ValueError(f'Request failed with status code: {code} and message: '
                             f'{resp.text}')
        
        resp = resp.json()
        
        result = {}
        result['id'] = resp['id']
        result['name'] = resp['name']
        result['height'] = resp['height']
        result['weight'] = resp['weight']
        result['base_exp'] = resp['base_experience']

        moves = []
        for move_dict in resp['moves']:
            moves.append(move_dict['move']['name'])
        
        result['moves'] = moves

        abilities = []
        for ability_dict in resp['abilities']:
            abilities.append(ability_dict['ability']['name'])
        
        result['abilities'] = abilities

        return result

    def get_pokemon_with_ability(self, ability):
        """
        Arguments:

        ability -- a lowercase string identifying an ability

        Returns a list of strings identifying pokemon that have the specified ability
        """
        req = f'ability/{ability}'
        resp = self.sess.get(f'{self.base_url}/{req}')

        code = resp.status_code
        if code != 200:
            raise ValueError(f'Request failed with status code: {code} and message: '
                             f'{resp.text}')

        pokemon = {}
        for poke_dict in resp.json()['pokemon']:
            tmp = poke_dict['pokemon']['url'][34:]
            pokemon[poke_dict['pokemon']['name']] = tmp[:-1]
        
        return pokemon

## -- Example usage -- ###
if __name__=='__main__':
    client = PokeClient()
    # l = client.get_pokemon_list()
    # ids = client.get_pokemon_ids()
    # print(ids[:10])

    # print(len(l))
    # print(l[1])

    i = client.get_pokemon_info("bulbasaur")
    print(i.keys())
    print(i['name'])
    print(i['base_exp'])
    print(i['weight'])
    print(i['height'])
    print(i['abilities'])
    print(len(i['moves']))
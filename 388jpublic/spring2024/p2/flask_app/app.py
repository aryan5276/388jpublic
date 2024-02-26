from flask import Flask, render_template
from .model import PokeClient
app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
poke_client = PokeClient()

@app.route('/', methods = ["GET"])
def index():
    """
    Must show all of the pokemon names as clickable links

    Check the README for more detail.
    """

    pokemon = poke_client.get_pokemon_list()
    ids = poke_client.get_pokemon_ids()
    return render_template('index.html', poke_list = zip(pokemon, ids))

@app.route('/pokemon/<pokemon_name>', methods = ["GET"])
def pokemon_info(pokemon_name):
    """
    Must show all the info for a pokemon identified by name

    Check the README for more detail
    """
    info = poke_client.get_pokemon_info(pokemon_name)

    return render_template('info.html', info=info)

@app.route('/ability/<ability_name>', methods = ["GET"])
def pokemon_with_ability(ability_name):
    """
    Must show a list of pokemon 

    Check the README for more detail
    """

    pokemons = poke_client.get_pokemon_with_ability(ability=ability_name)
    
    return render_template('ability.html', pokemon_dic=pokemons, ability=ability_name) 

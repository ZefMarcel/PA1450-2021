
# importing modules
from flask import Flask, render_template
  
# declaring app name
app = Flask(__name__)
  
# making list of pokemons
Pokemons =["Pikachu", "Charizard", "Squirtle", "Jigglypuff", 
           "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]
  
# defining home page
@app.route('/')
def homepage():

    return render_template('index.html', len = len(Pokemons), Pokemons = Pokemons)
  
if __name__ == '__main__':
  
    # running app
    app.run(use_reloader = True, debug = True)

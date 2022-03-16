from classes.dresseur import Dresseur
from functions.combat import combat
from random import randint
from functions.initiation import init


def game() :
    
    pokemonList = init()

    pseudo      = input('Quel est votre pseudo de dresseur ? ')

    pokemon_1   = input('Id de votre premier pokemon : ')
    pokemon_2   = input('Id de votre deuxième pokemon : ')
    pokemon_3   = input('Id de votre troisième pokemon : ')
    pokemon_4   = input('Id de votre quatrième pokemon : ')
    pokemon_5   = input('Id de votre cinquième pokemon : ')
    pokemon_6   = input('Id de votre dernier pokemon : ')

    pokemon_1 = pokemonList[int(pokemon_1) - 1]
    pokemon_2 = pokemonList[int(pokemon_2) - 1]
    pokemon_3 = pokemonList[int(pokemon_3) - 1]
    pokemon_4 = pokemonList[int(pokemon_4) - 1]
    pokemon_5 = pokemonList[int(pokemon_5) - 1]
    pokemon_6 = pokemonList[int(pokemon_6) - 1]

    adversaire = 'quentin'

    adversaire_1 = randint(0, 77)
    adversaire_2 = randint(0, 77)
    adversaire_3 = randint(0, 77)
    adversaire_4 = randint(0, 77)
    adversaire_5 = randint(0, 77)
    adversaire_6 = randint(0, 77)

    adversaire_1 = pokemonList[adversaire_1]
    adversaire_2 = pokemonList[adversaire_2]    
    adversaire_3 = pokemonList[adversaire_3]    
    adversaire_4 = pokemonList[adversaire_4]    
    adversaire_5 = pokemonList[adversaire_5]    
    adversaire_6 = pokemonList[adversaire_6]

    player = Dresseur(pseudo, [pokemon_1, pokemon_2, pokemon_3, pokemon_4, pokemon_5, pokemon_6])
    adversaire = Dresseur(adversaire, [adversaire_1, adversaire_2, adversaire_3, adversaire_4, adversaire_5, adversaire_6])
        
    
    combat(player, adversaire)

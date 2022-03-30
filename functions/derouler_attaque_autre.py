from functions.fonctions_attaque_autre import Abri, AntiBrume, Balance, BallMeteo, BlablaDodo, BouleRoc, BouteFeu, CasseBrique, ChocPsy, Clairvoyance, Clonage, CloseCombat, Colere, Conversion, Damocles, DracoMeteore, EclairFou, Effort, Explosion, Facade, FrappeAtlas, GlasDeSoin, LanceSoleil, Malediction, Megaphone


def Autres(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant, numAttaque) :
    if Attaque.id == 1 :
        pokemon_attaquant = Abri(pokemon_attaquant)
    elif Attaque.id == 2 :
        terrain = AntiBrume(terrain)
    elif Attaque.id == 8 :
        pokemon_attaquant, pokemon_defenseur = Balance(pokemon_attaquant, pokemon_defenseur)
    elif Attaque.id == 9 :
        pokemon_defenseur = BallMeteo(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 12 :
        pokemon_attaquant, pokemon_defenseur, terrain = BlablaDodo(pokemon_attaquant, pokemon_defenseur, terrain)
    elif Attaque.id == 15 :
        pokemon_defenseur = BouleRoc(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) 
    elif Attaque.id == 17 :
        pokemon_attaquant, pokemon_defenseur = BouteFeu(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) 
    elif Attaque.id == 20 :
        pokemon_defenseur = CasseBrique(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) 
    elif Attaque.id == 21 :
        print("ChangeEclair")
    elif Attaque.id == 22 :
        pokemon_defenseur = ChocPsy(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) 
    elif Attaque.id == 23 :
        pokemon_attaquant = Clairvoyance(pokemon_attaquant)
    elif Attaque.id == 24 :
        pokemon_attaquant = Clonage(pokemon_attaquant)
    elif Attaque.id == 25 :
        pokemon_attaquant, pokemon_defenseur = CloseCombat(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) 
    elif Attaque.id == 26 :
        pokemon_attaquant, pokemon_defenseur, dresseurPokemonAttaquant = Colere(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant, numAttaque)
    elif Attaque.id == 27 :
        pokemon_attaquant = Conversion(pokemon_attaquant)
    elif Attaque.id == 31 :
        pokemon_attaquant, pokemon_defenseur = Damocles(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 35 :
        print("DemiTour")
    elif Attaque.id == 36 :
        pokemon_attaquant, pokemon_defenseur = DracoMeteore(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 41 :
        pokemon_attaquant, pokemon_defenseur = EclairFou(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 43 :
        pokemon_defenseur = Effort(pokemon_attaquant, pokemon_defenseur)
    elif Attaque.id == 46 :
        pokemon_attaquant, pokemon_defenseur = Explosion(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 48 :
        pokemon_defenseur = Facade(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 50 :
        pokemon_defenseur = FrappeAtlas(pokemon_defenseur)
    elif Attaque.id == 51 :
        dresseurPokemonAttaquant = GlasDeSoin(dresseurPokemonAttaquant)
    elif Attaque.id == 61 :
        pokemon_defenseur, dresseurPokemonAttaquant = LanceSoleil(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant, numAttaque)
    elif Attaque.id == 67 :
        pokemon_attaquant, pokemon_defenseur = Malediction(pokemon_attaquant, pokemon_defenseur)
    elif Attaque.id == 70 :
        pokemon_defenseur = Megaphone(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 71 :
        print("NoeudHerbe")
    elif Attaque.id == 75 :
        print("Picots")
    elif Attaque.id == 76 :
        print("PicsToxik")
    elif Attaque.id == 77 :
        print("PiedSaute")
    elif Attaque.id == 78 :
        print("PiedVoltige")
    elif Attaque.id == 80 :
        print("PiegeDeRoc")
    elif Attaque.id == 91 :
        print("Projection")
    elif Attaque.id == 93 :
        print("PuissanceCachee")
    elif Attaque.id == 94 :
        print("Rapace")
    elif Attaque.id == 97 :
        print("Repos")
    elif Attaque.id == 98 :
        print("Requiem")
    elif Attaque.id == 100 :
        print("Sabotage")
    elif Attaque.id == 101 :
        print("Siphon")
    elif Attaque.id == 103 :
        print("Souvenir")
    elif Attaque.id == 105 :
        print("Stalagtite")
    elif Attaque.id == 106 :
        print("Surchauffe")
    elif Attaque.id == 108 :
        print("Surpuissance")
    elif Attaque.id == 109 :
        print("Synthese")
    elif Attaque.id == 113 :
        print("TourDeMagie")
    elif Attaque.id == 114 :
        print("TourRapide")
    elif Attaque.id == 118 :
        print("VampiPoing")
    elif Attaque.id == 119 :
        print("Vampigraine")
    elif Attaque.id == 120 :
        print("Vampirisme")
    elif Attaque.id == 121 :
        print("VentArriere")
    elif Attaque.id == 127 :
        print("Voeu")
    elif Attaque.id == 128 :
        print("VoleForce")
    

    return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant
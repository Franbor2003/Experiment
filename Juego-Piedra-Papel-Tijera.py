print("Programa de piedra/papel/tijera")
print ("==============================")
def jugar(p1, p2):
    if p1 == p2:
        return "Empate"
    elif p1 == "piedra":
        if p2 == "papel":
            return "Gana jugador 2: El papel envuelve a la piedra"
        else:
            return "Gana jugador 1: La piedra aplasta las tijeras"
    elif p1 == "papel":
        if p2 == "tijeras":
            return "Gana jugador 2: Las tijeras cortan el papel"
        else:
            return "Gana jugador 1: El papel envuelve la piedra"
    elif p1 == "tijeras":
        if p2 == "piedra":
            return "Gana jugador 2: La piedra aplasta las tijeras"
        else:
            return "Gana jugador 1: Las tijeras cortan el papel"


jugador1 = input("Jugador 1, elige piedra, papel o tijeras: ")
jugador2 = input("Jugador 2, elige piedra, papel o tijeras: ")
print ("=====================================================")

print(jugar(jugador1, jugador2))

import random

class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
        self.intentos_huir = 0
        self.items_utilizados = set()

    # Rest of the class methods...

def seleccionar_personaje():
    characters = {
        "1": "Mago",
        "2": "Héroe",
        "3": "Experto en Trampas"
    }
    print("Selecciona tu personaje:")
    for key, value in characters.items():
        print(f"{key}. {value}")

    while True:
        opcion = input("Elige un personaje (1-3): ")
        if opcion in characters:
            return Personaje(characters[opcion], 100)
        else:
            print("Opción no válida. Intenta de nuevo.")

def enfrentar_monstruo(personaje):
    monstruos = ["slime", "esqueleto", "araña", "fantasma"]
    monstruo_actual = random.choice(monstruos)

    print(f"Te has topado con un {monstruo_actual}. ¿Qué harás, {personaje.nombre}?")
    options = {
        "1": lambda: personaje.atacar_monstruo(),
        "2": lambda: (print(f"Lograste evadir al {monstruo_actual}. ¡Buena elección!") if personaje.intentos_huir < 3 else (
            print("Has intentado evadir tres veces consecutivas. ¡Debes combatir con las bestias ahora!"),
            setattr(personaje, "intentos_huir", 0))),
        "3": personaje.usar_pocion,
        "4": personaje.usar_escudo,
        "5": personaje.usar_bendicion,
        "6": personaje.usar_encantamiento,
        "7": personaje.usar_hierbas_medicinales,
        "8": personaje.usar_comida
    }

    while personaje.salud > 0:
        print("Opciones:")
        print("1. Atacar")
        print("2. Evadir")
        print("3. Usar poción")
        print("4. Usar escudo")
        print("5. Usar bendición")
        print("6. Usar encantamiento")
        print("7. Usar hierbas medicinales")
        print("8. Comer comida")

        opcion = input("Elige una opción (1-8): ")
        if opcion in options:
            options[opcion]()
        else:
            print("Opción no válida. Intenta de nuevo.")

    print("Tu personaje ha sido derrotado. ¡Fin del juego!")

def main():
    personaje = seleccionar_personaje()
    enfrentar_monstruo(personaje)

if __name__ == "__main__":
    main()
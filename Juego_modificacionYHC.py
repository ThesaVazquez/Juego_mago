import random

class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
        self.intentos_huir = 0
        self.items_utilizados = set()

    def atacar_monstruo(self):
        # Simula el ataque al monstruo
        return random.randint(10, 20)

    def recibir_dano(self, cantidad_dano):
        # Recibe daño del monstruo
        self.salud -= cantidad_dano
        print(f"Recibiste {cantidad_dano} de daño. Tu salud actual es {self.salud}.")

        if self.salud > 100:
            self.salud = 100
            print("¡Vida al máximo!")

    def usar_pocion(self):
        # Simula el uso de una poción para recuperar salud
        salud_recuperada = random.randint(20, 30)
        self.salud += salud_recuperada

        if self.salud > 100:
            self.salud = 100
            print("¡Vida al máximo!")
        else:
            print(f"Has usado una poción y recuperaste {salud_recuperada} de salud. ¡Ahora tu salud es {self.salud}!")

def seleccionar_personaje():
    print("Selecciona tu personaje:")
    print("1. Mago")
    print("2. Héroe")
    print("3. Experto en Trampas")

    opcion = input("Elige un personaje (1-3): ")
    
    if opcion == "1":
        return Personaje("Mago", 100)
    elif opcion == "2":
        return Personaje("Héroe", 100)
    elif opcion == "3":
        return Personaje("Experto en Trampas", 100)
    else:
        print("Opción no válida. Intenta de nuevo.")
        return seleccionar_personaje()

def enfrentar_monstruo(personaje):
    monstruos = {"slime", "esqueleto", "araña", "fantasma"}
    monstruo_actual = random.choice(list(monstruos))
    print(f"Te has encontrado con un {monstruo_actual}.")

    while personaje.salud > 0:
        print("Acciones disponibles:")
        print("1. Atacar")
        print("2. Huir")
        print("3. Usar item")

        accion = input("¿Qué acción deseas realizar? (1-3): ")

        if accion == "1":
            dano = personaje.atacar_monstruo()
            print(f"Has atacado al {monstruo_actual} y le has causado {dano} de daño.")

            if dano >= 15:
                print("¡Golpe crítico! El monstruo ha sido derrotado.")
                break
            else:
                print(f"El {monstruo_actual} sigue en pie.")

        elif accion == "2":
            personaje.intentos_huir += 1

            if personaje.intentos_huir >= 3:
                print("Has intentado huir demasiadas veces. El monstruo te ha atrapado.")
                personaje.recibir_dano(20)
                break
            else:
                print("Has intentado huir, pero el monstruo te lo impide.")

        elif accion == "3":
            print("Items disponibles:")
            print("1. Poción")
            print("2. Escudo")
            print("3. Bendición")
            print("4. Comida")
            print("5. Encantamiento")
            print("6. Hierbas medicinales")

            item = input("Selecciona un item para usar (1-6): ")

            if item == "1":
                if "poción" not in personaje.items_utilizados:
                    personaje.usar_pocion()
                    personaje.items_utilizados.add("poción")
                else:
                    print("Ya has utilizado una poción en esta batalla.")

            # Resto de opciones de items...

            else:
                print("Item no válido. Intenta de nuevo.")

        else:
            print("Acción no válida. Intenta de nuevo.")

    if personaje.salud <= 0:
        print("Has sido derrotado. Fin del juego.")
    else:
        print("¡Has derrotado al monstruo!")

def jugar():
    print("Bienvenido al juego de aventuras.")
    personaje = seleccionar_personaje()
    enfrentar_monstruo(personaje)

jugar()
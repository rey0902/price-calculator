import sys

game_prices_list = []
game_names_list = []

print()
print("Este es un programa para calcular el precio de juegos digitales")
print()
print('''Por favor selecciona la moneda en la que está el precio:
\t1.Pesos
\t2.Dólares
''')

# Function definitions


def dollar_calculation(price):
    calculation = price * 168.14
    return calculation


def pesos_calculation(price):
    calculation = price * 1.67
    return calculation


def append_data(name, price):
    game_names_list.append(name)
    game_prices_list.append(price)


def print_games(games_list1, games_list2):
    global total
    for index, game in enumerate(games_list1):
        print("\t{0} = ARS {1:.2f}".format(game,
                                           games_list2[index]))
    print("\tTotal = ARS {0:.2f}".format(total))


currency = "-"
options = ("pesos", "dolares")

# Creates a loop to ask user for input indefinitely until they select
# the correct option

while currency not in options:
    currency = input("Selecciona una opción: ")
    if currency == "1":
        print("Los precios que debes introducir son en pesos")
        currency = "pesos"
    elif currency == "2":
        print("Los precios que debes introducir son en dólares")
        currency = "dolares"
    else:
        print("Debe ser 1 o 2 para poder avanzar")

# Creates a loop to ask the user several times for input

core_loop = True

while core_loop:
    # Core section of the loop, makes calculations and appends to list
    game_name = input("Nombre del juego: ")
    try:
        game_price = float(input("Precio: "))
    except ValueError:
        print("Debe introducir un valor en numeros")
        sys.exit()
    if currency == "pesos":
        append_data(game_name, pesos_calculation(game_price))
    else:
        append_data(game_name, dollar_calculation(game_price))
    total = sum(game_prices_list)

    # Conditional statements to allow loop exit
    loop_exit_options = ("si", "no")
    answer = "-"
    while answer not in loop_exit_options:
        answer = input("Deseas ingresar otro juego?(si/no): ")
        if answer.casefold() == "no":
            print("El total a pagar es ARS {0:.2f}".format(total))
            core_loop = False
            break
        elif answer.casefold() == "si":
            pass
        else:
            print("La respuesta debe ser si o no")


# Asks the User if they require a list of the games
if len(game_names_list) > 1:
    list_prompt = input("Deseas una lista de los totales que "
                        "ingresaste?: ")
    if list_prompt.casefold() == "si":
        print()
        # For loop to allow to print a list regardless of the
        # qty of games
        print_games(game_names_list, game_prices_list)
    else:
        print("Cerramos el programa entonces")

# For loop pa la joda

for i in range(1, 10):
    print(i)
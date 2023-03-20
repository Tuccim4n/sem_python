from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
correctas = 0
incorrectas = 0
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")

for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)

    if (operator == "/") and (number_2 == 0):
        number_2 = randrange(1, 10)

# Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
# Le pedimos al usuario el resultado
    result = float(input("resultado: "))
    match operator:
        case "+": boolean = (result == (number_1 + number_2))
        case "-": boolean = (result == (number_1 - number_2))
        case "*": boolean = (result == (number_1 * number_2))
        case "/": boolean = (result == round(number_1 / number_2, 2))

    if (boolean):
        correctas += 1
        print("Es correcta")
    else:
        incorrectas += 1
        print("Es incorrecta")

                 
# Al terminar toda la cantidad de cuentas por resolver.
# SeD vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print("Cantidad de respuestas correctas: ", correctas, " e incorrectas: ", incorrectas)
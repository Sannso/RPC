from jsonrpclib import Server

def selectOperation():
    print('\tOperaciones básicas\n\n' +
        '¿Qué operación deseas realizar?\n\n' +
        '1. Suma\n' +
        '2. Resta\n' +
        '3. Multiplicación\n' +
        '4. División\n' +
        '5. Potencia\n' +
        '6. Logaritmo\n' +
        '7. Salir')

    op = readNumber(0)

    while op > 7 or op <= 0:
        print("\nLa opción seleccionada no existe.")
        op = readNumber(0)

    return op

def readNumber(index):
    number = 0

    while not number:
        try:
            if index == 1:
                number = int(input('\nPor favor, ingrese el primer número: '))
            elif index == 2:
                number = int(input('\nPor favor, ingrese el segundo número: '))
            else:
                number = int(input('\nPor favor, ingrese una opción: '))
            return number
        except:
            number = 0
            print("\nLo siento, debes ingresar un número valido.")

def main():
    conn = Server('http://localhost:1006')
    while True:
        op = selectOperation()

        if op == 7:
            break

        num1 = readNumber(1)
        num2 = readNumber(2)

        if op == 1:
            print(f'\nEl resultado de la suma es {conn.add(num1, num2)}\n')
        elif op == 2:
            print(f'\nEl resultado de la resta es {conn.substract(num1, num2)}\n')
        elif op == 3:
            print(f'\nEl resultado de la multiplicación es {conn.mul(num1, num2)}\n')
        elif op == 4:
            while not num2:
                print("\nEl divisor no puede ser cero.")
                num2 = readNumber(2)
            print(f'\nEl resultado de la división es {conn.div(num1, num2)}\n')
        elif op == 5:
            print(f'\nEl resultado de la potencia es {conn.pow(num1, num2)}\n')
        elif op == 6:
            print(f'\nEl resultado del logaritmo es {conn.log(num1, num2)}\n')
        

if __name__ == '__main__':
    main()
import json #Libreria para manejo de archivos JSON

#Funcion para desplegar el menu si encuentra el usuario
def consulta(array):
    pin=int(input("Ingrese su NIP: "))
    if(pin==array["pin"]):
        movimiento=1
        while movimiento==1:#Primero se define movimineto como 1 para que ejecute la primera vez el menu
            print("Seleccione el movimiento a realizar:")
            print("1. Consulta de saldo")
            print("2. Retiro")
            print("3. Deposito")
            print("4. Pago de servicios")
            print("5. Donar")
            print("6. Salir")
            opt=int(input())
            match opt:
                case 1:
                    saldo(array['pin'])
                case 2:
                    retiro(array['pin'])
                case 3:
                    deposito(array['pin'])
                case 4:
                    servicios()
                case 5:
                    retiro(array['pin'], True)
                case 6:
                    break #El break saca inmediatamente del for 
            movimiento=int(input("Ingrese 1 para realizar otro movimiento: "))#Cualquier dato distinto a 1 te saca alv
    else:
        print("PIN incorrecto")

#Funcion para mostrar el saldo
def saldo(pin):
    with open('BD.json') as database:
        data = json.load(database)
        for i in data['usuario']:
            if (pin == i['pin']):
                print('El saldo es de $', i['saldo'])
                break


# Función para retirar 
def retiro(pin, donacion):
    if (donacion):
        retirar = int(input('Cantidad a donar: '))
    else :
        retirar = int(input('Cantidad a retirar: '))

    with open('BD.json') as database:
        data = json.load(database)
        for i in data['usuario']:
            if (pin == i['pin']):
                if (retirar <= i['saldo']): # Verifica que el usuario tenga suficiente saldo
                    if (donacion):
                        print('Haz donado $', retirar, '. Muchas gracias!')
                    else :
                        print('Se han retirado $', retirar, ' de $', i['saldo'])
                    i['saldo'] = i['saldo'] - retirar
                    break
                else:
                    if (donacion):
                        print('No cuentas con el dinero suficiente para realizar esta donacion')
                    else :
                        print('No cuentas con la cantidad suficiente para retirar')
                    break

    with open('BD.json', 'w') as database:
        json.dump(data, database)

# Función para depositar
def deposito(pin):
    depositar = int(input('Cantidad a depositar: '))
    with open('BD.json') as database:
        data = json.load(database)
        for i in data['usuario']:
            if (pin == i['pin']):
                print('Se han depositado $', depositar, ' a $', i['saldo'])
                i['saldo'] = i['saldo'] + depositar
                    

    with open('BD.json', 'w') as database:
        json.dump(data, database)

def servicios():
    print("Aki va ooootra funcion")

while True: #Este while es para repetir el programa de forma indefinida
    print("Bienvenido.")
    id = int(input("Ingrese su usuario: "))
    with open("BD.json") as database:
        datos=json.load(database)#Lectura de los datos del JSON
        for i in datos["usuario"]:
            if(id==i["id"]):#Si coincide el id ingresado con alguno del JSON, abre la función
                consulta(i)
                break
            else:
                print("Error de datos. Intente nuevamente")
                break
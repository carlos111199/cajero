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
            print("5. Salir")
            opt=int(input())
            match opt:
                case 1:
                    saldo(array["saldo"])
                case 2:
                    retiro()
                case 3:
                    deposito()
                case 4:
                    servicios()
                case 5:
                    break #El break saca inmediatamente del for 
            movimiento=int(input("Ingrese 1 para realizar otro movimiento: "))#Cualquier dato distinto a 1 te saca alv
    else:
        print("PIN incorrecto")

#Funcion para mostrar el saldo
def saldo(saldo):
    print("Su saldo es de $", saldo)

#Funciones que hacen ustedes xdd
def retiro():
    print("Aki va una funcion")

def deposito():
    print("Aki va otra funcion")

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
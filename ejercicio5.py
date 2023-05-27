#Programa que realiza tipo de cambio de peso a dólar y viceversa.

cantidad = float(input("Ingrese la cantidad de dinero a convertir"))
tipo_cambio = input("¿Quiere convertir pesos a dólares (p-d) o dólares a pesos (d-p)?")

#Convertir la cantidad de dinero según el tipo de cambio solicitado

if tipo_cambio == "p-d" :
    conversion = cantidad / 480.0
    print("La cantidad de", cantidad, "pesos equivale a", conversion, "dólares")
elif tipo_cambio == "d-p" :
    conversion = cantidad * 480.0
    print("La cantidad de", cantidad, "dólares equivale a", conversion, "pesos")
else:
    print("El tipo de cambio ingresado no es válido, vuelva a intentar")
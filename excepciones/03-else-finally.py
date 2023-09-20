try:
    n1 = int(input("Ingresa el primer número: "))
except ValueError as ex:
    print("Ingrese un numero entero")
else: #Se ejecuta siempre y cuando no existan errores
    print("no ocurrio ninguna excepcion")
finally:
    print("Se ejecuta siempre")

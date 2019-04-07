dct = {"Ivan":"Profesor","Jamil":"Alumno","Jorge":"Informatico","Anna":"Contable"}
print("================== CALCULADORA ====================")
auto=str(input("Ingresa tu nombre para comprobar que estas autorizado\na utilizar este programa: "))
if auto in dct:
    dct==auto
    print("Genial!!! ",auto,"estas autorizado")
    input("Para continuar pulsa enter: ")
    print("¿Que Operación deseas realizar ?" "\na: Suma\nb: Resta\nc: Multiplicación\nd: División\ne: Exponencial" "\n")
    opc=(input("Ingresa una opción entre la a y e: "))
    num1=float(input("Ingresa tu primer número: "))
    num2=float(input("Ingresa tu segundo número: "))
    if opc == "a":
        suma = num1 + num2
        print(suma)
    if opc == "b":
        def resta(num1,num2):
            print(num1-num2)
        resta(num1,num2)
    if opc == "c":
        mult = num1 * num2
        print(multi)
    if opc == "d":
        try:
            div=num1/num2
        except ZeroDivisionError:
            div=0
            print(div,"!!!Este programa no acepta divisiones con 0!!!")

    if opc == "e":
        exp = num1 ** num2
        print(exp)
else:
    print("Lo siento!!! No estas autorizado")





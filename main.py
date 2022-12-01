print("\n****VENTAS****\n")

nombre = str(input("Ingrese su nombre: "))
nac= int(input("Ingrese su año de nacimiento: "))



if (nac<=2004):
    semestre1=float(input("Ingrese su venta del primer semestre:  "))
    semestre2=float(input("Ingrese su venta del segunda semestre: "))

    total=int(semestre1+semestre2)

    print("\nEl total es:", total)

    if semestre1>semestre2:
        mejor="1ero.(Primer semestre)"
    elif semestre2>semestre1:
        mejor="2do.(Segundo semestre)"

    if total<100000.00:
        premio="Un dia libre"
        medalla="Bronce"

    elif total< 500000.00:
        premio="Un dia libre con bono de Q250"
        medalla="Plata"
    elif  total < 1000000.00 :
        premio = "Un dia de libre y un bono de Q500"
        medalla = "0ro"
    else:
        premio = "Dos dias de libre y un bono de Q1000"
        medalla = "Diamante"

    print("")

    print("*****************************")
    print("\n")
    print("Vendedor: ", nombre)
    print("Ventas anuales : Q", total)
    print("Mejor semestre: ", mejor)
    print("Medalla acreditada: ", medalla)
    print("Premio: ", premio)
    print("")
    print("********************")
else:
    print("Menor de edad.")

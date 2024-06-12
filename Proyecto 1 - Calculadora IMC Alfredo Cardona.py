#Configurando las variables
Nombre = input("Su nombre por favor: ")
Edad = int(input("Su edad en años por favor: "))
Altura = float(input ("Su altura en metros con punto decimal por favor: "))
Peso = float (input("Su peso en kilogramos con punto decimal por favor : "))

IMC = Peso / Altura**2
if(Edad < 18):
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")
    print("Su IMC es de: " + str(IMC))
if IMC >= 0 and IMC <=15.99 :
    print ("Delgadez severa")
elif IMC >= 16.00 and IMC <=16.99 :
    print ("Delgadez moderada")
elif IMC >= 17.00 and IMC <=18.49 :
    print ("Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
    print ("Normal")
elif IMC >= 25.00 and IMC <= 29.99:
    print ("Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
    print ("Obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
    print ("Obesidad media")
elif IMC >= 40.00:
    print ("Obesidad morbida")
while True: 
       
 variable1= int(input('ingrese un numero'))
 print(" ")
 variable2= int(input('ingrese otro numero'))

 print(" ")
 print ("+.Suma")
 print ("-.Resta")
 print ("*.Multiplicacion")
 print ("/.Division")
 print("")
 print ("eliga el tipo de operacion que desea realizar:")
 eleccion= (input())

 if eleccion == '+':
        print(" ")
        print("Suma")
        print(f"resultado de sumas: {variable1+variable2}" )

 elif eleccion == '-':
        print(" ")
        print("Resta")
        print(f"resultado de restas: {variable1-variable2}")

 elif eleccion == '*':
        print(" ")
        print("Multiplicacion")
        print(f"resultado de multiplicacion: {variable1*variable2}")
        
 elif eleccion == '/':
        print(" ")
        print("Division")
        print(f"resultado de division: {variable1/variable2}") 
 else:
        print("te equivocastes de opcion")


 
 op = input("¿Quieres continuar? (si/no): ")

 if  op == "si":
        print("Ok, continuemos.")
 elif op == "no":
        print("Adiós.")
        break
 else:
        print("Error: Respuesta no válida. Por favor, ingresa 'si' o 'no'.")
        
 

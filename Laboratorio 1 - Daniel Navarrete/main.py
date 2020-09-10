'''
Nombre: Daniel Navarrete
'''


import sendMessage as SM
import receiveMessage as RM

seguir = True
while seguir:
   print("1. Enviar mensaje cifrado\n2. Recibir mensaje cifrado\n3. Salir")
   opcion = int(input("Ingrese una opcion: "))

   if opcion == 1:

      print(SM.sendMessage())

   elif opcion == 2:
      print(RM.receiveMessage())

   elif opcion == 3:
      seguir = False

   else:
      print("Error")

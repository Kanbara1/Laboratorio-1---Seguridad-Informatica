#Importaciones metodos de cifrado
import Vigenere as V
import vigenereTable as VT
import rotN as RN

#Importación libreria HASHLIB
import hashlib

def sendMessage():
   matriz = VT.vigenereTable()
   
   #Lectura de mensaje de entrada
   archivo = open("mensajedeentrada.txt","r")
   text = archivo.read().upper()

   #Cifrado de password para Vigenere
   pw = "dnavarreter".upper()
   pw = RN.rotN(pw,-5)

   #Proceso de cifrado de mensaje
   text = RN.rotN(text,-8)
   text = V.encode(matriz,pw,text)
   text = RN.rotN(text,20)

   #Obtencion de hash
   Hash = hashlib.sha1()
   Hash.update(text.encode('utf-8'))
   vHash = Hash.hexdigest()

   #Creacion de mensaje seguro
   archive = open("mensajeseguro.txt","w")
   archive.write(text)
   archive.close()

   archiveHash = open("hash.txt","w")
   archiveHash.write(vHash)
   archiveHash.close()

   return "Mensaje Enviado"


   









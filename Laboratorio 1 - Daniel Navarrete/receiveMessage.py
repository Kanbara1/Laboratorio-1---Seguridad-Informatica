#Importaciones metodos de cifrado
import Vigenere as V
import vigenereTable as VT
import rotN as RN

#Importación libreria HASHLIB
import hashlib


def receiveMessage():
   matriz = VT.vigenereTable()

   #Cifrado de password para Vigenere
   pw = "dnavarreter".upper()
   pw = RN.rotN(pw,-5)

   #Obtención de hash original
   archiveHash = open("hash.txt","r")
   oHash = archiveHash.read()
   
   #Lectura de mensaje recivido
   archivo = open("mensajeseguro.txt","r")
   text = archivo.read()

   #Validacion de hash
   Hash = hashlib.sha1()
   Hash.update(text.encode('utf-8'))
   vHash = Hash.hexdigest()
   
   if(oHash == vHash):
      text = RN.rotN(text,-20)
      text = V.decode(matriz,pw,text)
      text = RN.rotN(text,8)
      return text

   else:
      return "MENSAJE ADULTERADO"

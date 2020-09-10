def vigenereTable():
   archivo = open("vigenereTable.csv","r")

   matriz = []
   for linea in archivo:
      temp = []
      for x in linea.split(";"):
         if "\n" in x:
            x.split("\n")
            temp.append(x[0])
         else:
            temp.append(x)
            
         
      matriz.append(temp)
      matriz[0][0] = "A"

   archivo.close()
   return matriz

def encode(matriz,pw,text):
   text = text.upper()
   pw = pw.upper()
   
   largopw = len(pw)
   largotx = len(text)
   cont = 0
   
   data = ""
   data = data.join(matriz[0])
   result = ""
   
   for i in range(0,largotx):
      if(text[i] == " "):
         result += " "
      elif(cont == largopw-1):
         pos1 = data.find(pw[cont])
         pos2 = data.find(text[i])
         result += matriz[pos1][pos2]
         cont = 0
      
      else:
         pos1 = data.find(pw[cont])
         pos2 = data.find(text[i])
         result += matriz[pos1][pos2]
         cont+=1
   return result

def decode(matriz,pw,text):
   text = text.upper()
   pw = pw.upper()
   
   largopw = len(pw)
   largotx = len(text)
   cont = 0

   data = ""
   data = data.join(matriz[0])
   resultado = ""
   
   for i in range(0,largotx):
      if(text[i] == " "):
         resultado += " "
      elif(cont == largopw-1):
         pos1 = data.find(pw[cont])
         temp = "".join(matriz[pos1])
         pos2 = temp.find(text[i])
         resultado += matriz[0][pos2]
         cont = 0
      
      else:
         pos1 = data.find(pw[cont])
         temp = "".join(matriz[pos1])
         pos2 = temp.find(text[i])
         resultado += matriz[0][pos2]
         cont += 1
   return resultado
      

def rotN(text,Pos):
    rot = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    textoRot = ""

    for letra in text:
        largo = len(rot)
        pos=-1
        pos=rot.find(letra)
        if(pos>=0):
            pos+=Pos
            if(pos>=largo):
               pos-=largo
            textoRot += str(rot[pos])
        else:
            textoRot += str(letra)

    return textoRot

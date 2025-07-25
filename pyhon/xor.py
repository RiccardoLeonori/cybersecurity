stringa:str = "Nel mezzo del cammin di nostra vita"
lista:list = []
lista2:list = []
stringaDecodificata:str = ""
xor:int = int(input("Dammi lo xor: "))

for i in stringa:
    lista.append(ord(i) ^ xor)
    
print(lista)

for i in lista:
    lista2.append(i ^ xor)

print(lista2)

for i in lista:
    stringaDecodificata += (chr(i ^ xor))

print(stringaDecodificata)
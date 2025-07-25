'''stringa:str = "Nel mezzo del cammin di nostra vita"
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

print(stringaDecodificata)'''

from functools import reduce

msg = input("Dammi il messaggio: ")
key = int(input("Dammi la chiave: "))

cifrato = [ord(c)^key for c in msg]
# la precedente può essere scritta come un for semplice
cifrato=[]
for c in msg:
    cifrato.append(ord(c)^key)

print("Messaggio cifrato: ", cifrato)

# Ora decifro

#Uso la comprhension
decifrato = ''.join([chr(c^key) for c in cifrato])
# la precedente può essere scritta come un for semplice
decifrato = []
for c in cifrato:
    decifrato.append(chr(c^key))
decifrato = ''.join(decifrato)
print("Messaggio decifrato: ", decifrato)
# Nota: join è un metodo delle stringhe, non una funzione globale
# Quindi non posso fare join(cifrato) ma devo fare ''.join(cifrato)
# oppure usare join(cifrato) se cifrato è una lista di stringhe
# oppure ''.join(cifrato) se cifrato è una lista di caratteri
# oppure ''.join(map(chr, cifrato)) se cifrato è una lista di interi

print(reduce(lambda x,y: x+y, map(lambda x : chr(x ^ key), map(lambda c: ord(c) ^ key, list(msg))), ""))
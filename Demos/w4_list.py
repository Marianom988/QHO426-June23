#Declare empty list
bleh = []
meh = list()
#Declare non-empty list
yummy = ["pizza", "mozzarella", "chocolate"]

print(yummy)
#Print a single item . il primo item della lista e' il numero 0
print(yummy[-2])
#print some item from the list i due punti significano "fino a" in questo caso da 1 a 3
print(yummy[::-1]) # i valori funzionano come nella funzione range . start, end, step
#[::-1] reverse
#expand the list , partiamo da quella vuota
# .append aggiunge item alla fine
print(bleh)
bleh.append("spinach")
bleh.append("broccoli")
bleh.append("aubergine")
bleh.append("pesto")
print (bleh)
#.extend aggiunge item to a list
bleh.extend(["liver","tomatos"])
print(bleh)
#.remove rimuove items. se mettiamo if e un item provera' a cercare e rimuovere l'item senza dare errore
if"hot dog" in bleh:
    bleh.remove("broccoli")
print(bleh)
#con .insert puoi dare una posizione precisa all'item. specifica la posizione seguito da comma e poi l'item
bleh.insert(1,"carrot")
print(bleh)
bleh.insert(4,"cabbage")
print(bleh)
# .pop rimuove specifici items (bisogna indicare la posizione tra parentesi dell'item da eliminare)
# possiamo dare anche un valore all'item rimosso
x = bleh.pop(3)
bleh.pop(3)
bleh.pop(5)
print (bleh)
print (x)
# mutate ovvero replace un item con un altro. nome_lista[poiszione item da sositutire]
print(yummy)
yummy[2] = "pancacke"
print(yummy)
#sommare elementi di una lista
lista = ["fred", 56, True, 99.4, "Potato", False,82]
sum = 0
for item in lista:
    if isinstance(item,int):
        sum += item

print(sum)

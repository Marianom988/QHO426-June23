#open file for reading
f = open("files/song.txt")
#Print single line
# print(f.readline(), end="")
# print(f.readline(), end="")
#print full content of the file
# print(f.read(10)) # senza parametri stampa tutto, con numero stampa tanti caratteri quanto il numero
#grab content of txt file and save it as a list
lista = f.readlines()
print(lista)
print(lista[2])
f.close() # close file to make it available again
g = open("files/song.txt", "a")
#write a single line into the end of the file
g.write("\nAnd it's everlasting, infinite\n")
#write multiple lines into a file
g.writelines(["it goes on and on, you can't measure it\n", "Can't quench your love\n "])
g.close()
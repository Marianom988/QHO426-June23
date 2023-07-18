def adding(lista = []):
    new_member = input("Enter name of new avenger:\n")
    lista.append(new_member)

def remove(lista = []):
    rejected = input("Enter the avenger to be removed:\n")
    if rejected in lista:
        lista.remove(rejected)
#
# a = ["fred", "geroge", "harry", "anna"]
# remove(a)
# print(a)

def printing(lista = []):
    for hero in lista:
         print(f"The mighty {hero} is part of the avengers")

# x = ["kelly", "Jerzy", "victoria", "Marius"]
# printing(x)



def run():
    avengers = []
    while True:
     opt = int(input("Avengers, Assemble!\n\n1-Add an Avenger\n2-Remove an Avenger\n3-Check on the Team\n4-Exit"))
     if opt ==1:
        adding(avengers)
     elif opt ==2:
         remove(avengers)
     elif opt ==3:
         printing(avengers)
     elif opt ==4:
         break
     else:
         print("No such option. Go to Spacesavers")

run()
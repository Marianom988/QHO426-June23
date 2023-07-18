def generate():
    name = input("Enter name: ")
    mrk = float(input("Enter the mark: "))
    return name,mrk
#
# print(generate())
# x = generate()
# print(x)
# print(type(x)) per controllare cosa e' x

def list_of_students(n):
    stud_list = []
    for i in range(n):
        stud_list.append(generate())
    return stud_list

# print(list_of_students(3))

def average(lista = []):
    total = 0
    for tup in lista:
        total += tup[1]
    avg = total/len(lista)
    return avg

def run():
    s_list = []
    while True:
        opt = int(input("Menu:\n\n1-Populate list of students\n2-Calculate average mark\n3-Change mark of one student\n4-Exit\nChoise: "))
        if opt ==4:
            break
        elif opt == 1:
            num = int(input("How many student would you like to add?"))
            s_list.extend(list_of_students(num))
        elif opt == 2:
            print(f"The average mark is {average(s_list):.2f}")
        elif opt ==3:
            name = input("Whose mark is to be changed")
            for student in s_list:
                if name == student[0]:
                    n_mark = float(input("Enter new mark: "))
                    s_list.remove(student)
                    s_list.append((name, n_mark))
        else:
            print("No such option. Try again. Fool!")

run()

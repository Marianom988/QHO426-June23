# with open("books.txt","x"):
#     print()

# with open("books.txt","w") as f:
#     lines = ["Section: The Law Section\n","The Magna carta\n","Section: The Technology Section\n","How to build a robot\n","How to build a flying car\n","Section: The History Section\n","The  History of Everything"]
#     f.writelines(lines)

def search(boos):
    print("Searching...")
    sections = []
    books = []
    with open(boos) as red:
        for i in red.readlines():
            f = i.strip("\n")
            if f.startswith("Section"):
                g = f.replace(i[0:9], "")
                sections.append(g)
            else:
                books.append(f)
        print(f"Sections:{sections}\nBooks:{books}")

search("books.txt")

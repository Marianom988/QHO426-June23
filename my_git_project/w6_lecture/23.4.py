def search():
    print("Searching...")
    data = {}
    with open("books.txt") as f:
        for i in f.readlines():
            if i.startswith("Section"):
                g = i.replace(i[0:9], "")
                return g
            else:
                section = i
                data.update(section)

search()

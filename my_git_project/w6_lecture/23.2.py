# file = open("location.txt","x")
# file.close()

# with open("location.txt","w") as classes:
#     classes.write("The Art Section\nThe Law Section\nThe Technology Section\nThe History section")
#
def search(location):
    print("Searching...")
    with open(location) as x:
        for row in x.readlines():
            print(f"Looked in {row.strip()}")
        print("Done!")


def run():
    search("location.txt")

run()
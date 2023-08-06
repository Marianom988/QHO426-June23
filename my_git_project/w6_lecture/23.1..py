import os #importa il module os


def cwd():
    path = os.getcwd()#per mostrare la current working directory
    print(f"The current Working directory is {path}")
    print(f"the Directory contains the following:")
    for file in os.listdir(path):# Per mostrare la lista di quello che la directory contiene
        print(file)

def run():
    print("Processing...")
    cwd()

run()

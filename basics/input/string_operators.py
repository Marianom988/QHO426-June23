lives = int(input("Please enter the number of lives.\n"))
energy = int(input("Please enter the energy level.\n"))
shield = int(input("Please enter the shield level.\n"))
print("Healt has been set.\n")
print(f"Lives:\t", lives * "♥")
print(f"Energy:\t", energy * "♦")
print(f"Shield:\t", shield * "♦")

print("Lives:\t" + "\u2764"* lives)
print(f"Lives:\t" + lives * "♥")

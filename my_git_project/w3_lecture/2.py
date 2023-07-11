print("Program started")
f = int(input("Please enter an ASCII code:\n"))
if f in range(32,126+1):
    g = chr(f)
    print(f"The character representerd by the ASCII code {f} is {g}")
print("Program Endend")

f = int(input("What level of brightness is required?\n"))
print("adjusting brightness...\n")
for i in range(2,f+1,2):
    print(f"Beep Brightness level", "#"*i,"\nBop Brightness level", "#"*i,"\n")


n=input("Enter the string:")
x=len(n)
for i in range(x):
    for j in range(i+1):
        print(n[j],end="")
    print()

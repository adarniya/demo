a=1
b=0
for i in range(4):
    for j in range(i):
        print(b,end=" ")
        b = a + i
    print()
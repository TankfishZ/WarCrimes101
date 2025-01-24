n = int(input("Enter:"))
c1 = 0
c2 = 1
total = 0
if n == 1:
    print(0)
elif n == 2:
    print(0,1)
else:
    print(c1)
    print(c2)
    for i in range (n-2):
        total = c1+c2
        c1=c2
        c2=total
        print(total)
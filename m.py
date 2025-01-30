m = 0
for i in range(3):
    n = int(input("Enter your number:"))
    if i == 0:
        m = n
    elif n<m:
        m=n
print(m)



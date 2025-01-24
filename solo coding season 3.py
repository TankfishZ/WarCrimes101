n = int(input("Enter your number please I don't want to do reverse no more:"))
h = 0
while n>0:
    h = h*10 + n % 10
    n = n//10
    

print(h)
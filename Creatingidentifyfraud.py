n = (input("Enter your citizen id to commit identify fraud: "))
i = 0
t=0
for m in range(13,1,-1):
    t = t+m*int(n[i])
    i+=1
s=(11-(t)%11)%10
print(s)
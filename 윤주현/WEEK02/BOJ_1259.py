lst = []
while True :
    n = input()
    if n == '0' :
        break
    lst.append(n)

for i in lst :
    a = 'yes'
    for j in range(len(i)//2) :
        if i[j] != i[-j-1] :
            a = 'no'
            break
    print(a)
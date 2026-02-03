lst = []

while True :
    a1, b1, c1 = map(int, input().split())
    if a1 == b1 == c1 == 0 :
        break
    lst.append([a1, b1, c1])

for i in range(len(lst)) :
    lst[i].sort()
    a, b, c = lst[i]
    
    if a**2 + b**2 == c**2 :
        print('right')
    else :
        print('wrong')
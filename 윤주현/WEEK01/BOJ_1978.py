n = int(input())
lst = list(map(int, input().split()))
ans = 0

for i in lst :
    temp = 0
    for j in range(2, i) :
        if i%j == 0 :
            temp += 1
    if i != 1 and temp == 0 :
        ans += 1

print(ans)
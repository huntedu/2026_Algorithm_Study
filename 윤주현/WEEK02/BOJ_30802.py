N = int(input())
size_lst = list(map(int, input().split()))
T, P = map(int, input().split())

Tc = 0
for i in size_lst :
    if i%T == 0 :
        Tc -= 1
    Tc += (i//T + 1)
print(Tc)

print(N//P, N%P)
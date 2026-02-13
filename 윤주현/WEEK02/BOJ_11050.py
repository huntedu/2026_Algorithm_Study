N, K = map(int, input().split())

k = K
a, b = 1, 1

for _ in range(K) :
    a *= N
    b *= k
    N -= 1
    k -= 1

print(a//b)
a = list(map(int, input().split()))
r = list(map(int, input().split()))

ans = 0
for i in range(3):
    if r[i] > a[i]:
        ans += r[i] - a[i]

print(ans)
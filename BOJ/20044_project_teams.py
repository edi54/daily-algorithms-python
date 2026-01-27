import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

l, r = 0, 2 * n - 1
ans = 10**18

while l < r:
    ans = min(ans, arr[l] + arr[r])
    l += 1
    r -= 1

print(ans)
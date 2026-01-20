import sys
input = sys.stdin.readline
n = int(input().strip())
B = list(map(int, input().split()))
A = []
prefix_sum = 0
for i in range(n):
    current = B[i] * (i + 1) - prefix_sum
    A.append(current)
    prefix_sum += current
print(*A)
import sys
input = sys.stdin.readline
N = int(input())
MOD = 1_000_000
if N == 1:
    print(1)
    exit(0)
dp = [[[0] * 2 for _ in range(N + 1)] for __ in range(N + 1)]
dp[1][1][0] = 1
dp[1][1][1] = 1
dp[2][1][0] = 1
dp[2][2][1] = 1
for i in range(3, N + 1):
    for j in range(1, i + 1):
        s1 = 0
        for k in range(1, j):
            s1 += dp[i - 1][k][0]
        dp[i][j][1] = s1 % MOD
        s0 = 0
        for k in range(j, i):
            s0 += dp[i - 1][k][1]
        dp[i][j][0] = s0 % MOD
ans = 0
for j in range(1, N + 1):
    ans = (ans + dp[N][j][0] + dp[N][j][1]) % MOD
print(ans)
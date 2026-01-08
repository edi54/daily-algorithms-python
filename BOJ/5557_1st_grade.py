import sys
input = sys.stdin.readline
N = int(input().strip())
nums = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(N-1)]
dp[0][nums[0]] = 1
for i in range(1, N-1):
    x = nums[i]
    for v in range(21):
        if dp[i-1][v] > 0:
            nv = v + x
            if 0 <= nv <= 20:
                dp[i][nv] += dp[i-1][v]
            nv = v - x
            if 0 <= nv <= 20:
                dp[i][nv] += dp[i-1][v]
print(dp[N-2][nums[N-1]])
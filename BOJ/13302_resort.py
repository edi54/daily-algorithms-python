import sys
from functools import lru_cache
input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    closed = set(map(int, input().split())) if M else set()
    @lru_cache(None)
    def dp(day, coupon):
        if day > N:
            return 0
        if day in closed:
            return dp(day + 1, coupon)
        cost = 10000 + dp(day + 1, coupon)
        cost = min(cost, 25000 + dp(day + 3, coupon + 1))
        cost = min(cost, 37000 + dp(day + 5, coupon + 2))
        if coupon >= 3:
            cost = min(cost, dp(day + 1, coupon - 3))
        return cost
    print(dp(1, 0))
if __name__ == "__main__":
    solve()
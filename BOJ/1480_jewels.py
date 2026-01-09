import sys
from functools import lru_cache
input = sys.stdin.readline
N, M, C = map(int, input().split())
weights = list(map(int, input().split()))
@lru_cache(None)
def dfs(bag: int, used: int, remain: int) -> int:
    """
    bag   : 현재 가방 인덱스
    used  : 사용된 보석 비트마스크
    remain: 현재 가방의 남은 용량
    """
    if bag == M:
        return 0
    best = dfs(bag + 1, used, C)
    for i in range(N):
        if used & (1 << i):
            continue
        if weights[i] > remain:
            continue
        best = max(best, 1 + dfs(bag, used | (1 << i), remain - weights[i]))
    return best
def main():
    print(dfs(0, 0, C))
if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    main()
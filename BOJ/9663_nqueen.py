import sys
sys.setrecursionlimit(10**7)

def main():
    n = int(sys.stdin.readline().strip())
    mask = (1 << n) - 1
    ans = 0

    def dfs(row, cols, diag1, diag2):
        nonlocal ans
        if row == n:
            ans += 1
            return

        available = mask & ~(cols | diag1 | diag2)
        while available:
            pick = available & -available
            available -= pick
            dfs(
                row + 1,
                cols | pick,
                ((diag1 | pick) << 1) & mask,  
                (diag2 | pick) >> 1
            )

    dfs(0, 0, 0, 0)
    print(ans)

if __name__ == "__main__":
    main()
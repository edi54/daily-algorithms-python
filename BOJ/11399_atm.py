import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    p = list(map(int, input().split()))
    p.sort()

    prefix = 0
    ans = 0
    for x in p:
        prefix += x
        ans += prefix

    print(ans)

if __name__ == "__main__":
    main()
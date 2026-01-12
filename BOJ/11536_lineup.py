import sys
input = sys.stdin.readline
def main():
    n = int(input().strip())
    names = [input().strip() for _ in range(n)]
    if names == sorted(names):
        print("INCREASING")
    elif names == sorted(names, reverse=True):
        print("DECREASING")
    else:
        print("NEITHER")
if __name__ == "__main__":
    main()
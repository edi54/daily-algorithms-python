import sys

def main():
    N, r, c = map(int, sys.stdin.readline().split())
    ans = 0
    size = 1 << N

    while N > 0:
        half = size >> 1
        block = half * half

        if r < half and c < half:
            pass
        elif r < half and c >= half:
            ans += block
            c -= half
        elif r >= half and c < half:
            ans += block * 2
            r -= half
        else:
            ans += block * 3
            r -= half
            c -= half

        size = half
        N -= 1

    sys.stdout.write(str(ans))

if __name__ == "__main__":
    main()
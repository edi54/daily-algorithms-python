import sys
def solve():
    n, m = map(int, sys.stdin.readline().split())
    a, b = n, m
    turn = 0  
    while True:
        if a < b:
            a, b = b, a
        if b == 0:
            winner = 1 - turn
            break
        if a % b == 0 or a >= 2 * b:
            winner = turn
            break
        a = a - b
        turn ^= 1
    print("win" if winner == 0 else "lose")
if __name__ == "__main__":
    solve()
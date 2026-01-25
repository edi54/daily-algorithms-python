import sys
def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dna = [input().strip() for _ in range(n)]
    order = ['A', 'C', 'G', 'T']
    consensus = []
    dist = 0
    for j in range(m):
        cnt = {c: 0 for c in order}
        for i in range(n):
            cnt[dna[i][j]] += 1
        best_char = order[0]
        best_count = cnt[best_char]
        for c in order[1:]:
            if cnt[c] > best_count:
                best_char = c
                best_count = cnt[c]
        consensus.append(best_char)
        dist += n - best_count
    print("".join(consensus))
    print(dist)
if __name__ == "__main__":
    solve()
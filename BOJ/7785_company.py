n = int(input())
enter_log = set()
for _ in range(n):
    k, v = input().split()
    if v == "enter":
        enter_log.add(k)
    else:
        enter_log.discard(k)
print("\n".join(sorted(enter_log, reverse=True)))
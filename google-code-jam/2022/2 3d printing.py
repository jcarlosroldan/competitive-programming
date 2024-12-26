T = int(input())
for case in range(1, T + 1):
    print('Case #%s: ' % case)
    printers = [
        list(map(int, input().split()))
        for _ in range(3)
    ]
    res = [min(color) for color in zip(*printers)]
    remaining = 1e6
    for c in range(4):
        res[c] = int(min(remaining, res[c]))
        remaining -= res[c]
    print('IMPOSSIBLE' if remaining else ' '.join(map(str, res)))
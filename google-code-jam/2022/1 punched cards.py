T = int(input())
for case in range(1, T + 1):
    print('Case #%d:' % case)
    R, C = map(int, input().split())
    res = [('+-' * C) + '+\n' + ('|.' * C) + '|' for _ in range(R)] + ['+-' * C + '+']
    n = C * 2 + 2
    res[0] = '..' + res[0][2:n] + '.' + res[0][n + 1:]
    print('\n'.join(res))
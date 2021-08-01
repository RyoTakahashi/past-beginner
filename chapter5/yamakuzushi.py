# 第二回PAST　C問題　https://atcoder.jp/contests/past202004-open/tasks/past202004_c
n = int(input())
s = [list(input()) for _ in range(n)]

for i in reversed(range(0,n-1)):
    for j in range(1,2*n-1):
        if s[i][j] == "#":
            look_lst = [s[i+1][k] for k in range(j-1,j+2)]
            if "X" in look_lst:
                s[i][j] = "X"

for i in range(0, len(s)):
    print(''.join(s[i]))
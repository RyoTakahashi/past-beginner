# 第三回PAST E問題 (https://atcoder.jp/contests/past202005-open/tasks/past202005_e)
n, m, q = map(int, input().split())
e_lst = [[] for _ in range(n)]
for i in range(m):
    s, t = map(int, input().split())
    e_lst[s-1].append(t-1)
    e_lst[t-1].append(s-1)

c_lst = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    print(c_lst[query[1] - 1])
    if query[0] == 1:
        # スプリンクラー起動
        for v in e_lst[query[1] - 1]:
            c_lst[v] = c_lst[query[1] - 1]
    else:
        # 色上書き
        c_lst[query[1] - 1] = query[2]
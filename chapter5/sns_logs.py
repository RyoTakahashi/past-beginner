# 第一回PAST E問題 https://atcoder.jp/contests/past201912-open/tasks/past201912_e
n, q = map(int, input().split())
# 各ユーザが誰をフォローしているのかのリスト
f_lst = [[] for _ in range(n+1)]
# 各ユーザが誰にフォローされているのかのリスト
f_lst_inv = [[] for _ in range(n+1)]

for _ in range(q):
    action = list(map(int,input().split()))
    if action[0] == 1:
        f_lst[action[1]].append(action[2])
        f_lst_inv[action[2]].append(action[1])
        f_lst_inv[action[2]] = list(set(f_lst_inv[action[2]]))
    elif action[0] == 2:
        t_lst = f_lst_inv[action[1]]
        for i in range(len(t_lst)):
            f_lst[action[1]].append(t_lst[i])
    else:
        t_lst = f_lst[action[1]]
        for i in range(len(t_lst)):
            t_lst2 = f_lst[t_lst[i]]
            for j in range(len(t_lst2)):
                f_lst[action[1]].append(t_lst2[j])
                f_lst_inv[t_lst2[j]].append(action[1])
                f_lst_inv[t_lst2[j]] = list(set(f_lst_inv[t_lst2[j]]))

    f_lst[action[1]] = list(set(f_lst[action[1]]))

for i in range(1,len(f_lst)):
    res = ''
    for j in range(1,n+1):
        if (i != j) and (j in f_lst[i]):
            res = res + 'Y'
        else:
            res = res + 'N'
    print(res)

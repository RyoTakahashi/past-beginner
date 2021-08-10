# ABC161 D (https://atcoder.jp/contests/abc161/tasks/abc161_d)
from collections import deque
K = int(input())

if K <= 10:
    print(K)
    exit()

Q = deque()
# 初期化
cnt = 9
for i in range(1,10):
    Q.append(i)
    
while len(Q) > 0:
    i = Q.popleft()
    t_num = int(str(i)[-1])
    for j in [t_num-1, t_num, t_num+1]:
        if (j == 10) or (j == -1):
            continue
        next = int(str(i) + str(j))
        # Qをリフレッシュする
        Q.append(next)
        cnt += 1
        if cnt == K:
            print(next)
            exit()
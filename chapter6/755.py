# ABC114 C (https://atcoder.jp/contests/abc114/tasks/abc114_c)
from collections import deque
N = int(input())

def bfs(Q: deque) -> int:
    global cnt
    while len(Q) > 0:
        i = Q.popleft()  
        if i[1] and i[2] and i[3]:
            cnt += 1   
        for j in ['3', '5', '7']:
            n = int(str(i[0]) + j)
            if n <= N:
                if j == '3':
                    Q.append((n, True, i[2], i[3]))
                elif j == '5':
                    Q.append((n, i[1], True, i[3]))
                else:
                    Q.append((n, i[1], i[2], True))
    
    return cnt

cnt_all = 0
cnt = 0
for i, x in enumerate([3,5,7]):
    cnt = 0
    tmp = [x, False, False, False]
    tmp[i+1] = True
    Q = deque()
    Q.append(tuple(tmp))
    cnt_all += bfs(Q)
    
print(cnt_all)


"""
N = int(input())

cnt = 0

def dfs(d, flg3, flg5, flg7):
    global cnt
    if d > N:
        return
    
    if flg3 and flg5 and flg7:
        cnt += 1
    
    dfs(10*d+3, True, flg5, flg7)
    dfs(10*d+5, flg3, True, flg7)
    dfs(10*d+7, flg3, flg5, True)

dfs(0, False,False,False)

print(cnt)
    
"""
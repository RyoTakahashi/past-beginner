# ABC007 C (https://atcoder.jp/contests/abc007/tasks/abc007_3)
from collections import deque
r, c = map(int, input().split())
sx, sy = map(int,input().split())
gx, gy = map(int,input().split())

mat = []
p_mat = []
p = 0
visited = []
for _ in range(r):
    r_i = list(input())
    mat.append(r_i)
    p_mat.append([p+i for i in range(0,c)])
    visited.extend([-1 for _ in range(0,c)])
    p += c

# 辺リストを作成する
e_dict = {}
for i in range(1, r):
    for j in range(1,c):
        if mat[i][j] == ".":
            tmp_l = []
            if mat[i-1][j] == ".":
                tmp_l.append(p_mat[i-1][j])
            if mat[i][j-1] == ".":
                tmp_l.append(p_mat[i][j-1])
            if mat[i+1][j] == ".":
                tmp_l.append(p_mat[i+1][j])
            if mat[i][j+1] == ".":
                tmp_l.append(p_mat[i][j+1])
            e_dict[p_mat[i][j]] = tmp_l

# スタート地点とゴール地点の番号取得
s = p_mat[sx-1][sy-1]
g = p_mat[gx-1][gy-1]

# BFS
Q = deque()
Q.append(s)
visited[s] = 0

while len(Q) > 0:
    i = Q.popleft()
    for j in e_dict[i]:
        if visited[j] == -1:
            visited[j] = visited[i] + 1
            Q.append(j)
        if g in Q:
            print(visited[g])
            exit()

    
    
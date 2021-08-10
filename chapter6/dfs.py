# ATC001 A (https://atcoder.jp/contests/atc001/tasks/dfs_a)
# おまじない
import sys
sys.setrecursionlimit(1000000)

H, W = map(int, input().split())

grids = [['#']*(W+2)]
visited = [[True]*(W+2)]
for i in range(H):
    tmp = ['#'] + list(input()) + ['#']
    tmp_v = [True] + [False]*len(tmp) + [True]
    grids.append(tmp)
    visited.append(tmp_v)
    if 's' in tmp:
        sx = i + 1
        sy = tmp.index('s')
grids.append(['#']*(W+2))
visited.append([True]*(W+2))

def dfs(i, j):
    visited[i][j] = True
    for next in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        if not visited[next[0]][next[1]]:
            if grids[next[0]][next[1]] == 'g':
                print('Yes')
                exit()
            if grids[next[0]][next[1]] == '.':
                dfs(next[0], next[1])

dfs(sx, sy)
print('No')
    






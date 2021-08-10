# 第三回PAST G (https://atcoder.jp/contests/past202005-open/tasks/past202005_g)
from collections import deque, defaultdict
N, gx, gy = map(int, input().split())

# 初期化
grids = defaultdict(lambda: ".")

for _ in range(N):
    # 障害物配置
    grids[tuple(map(int, input().split()))] = '#'

# 外壁（ゴールのx座標y座標ともに-200~200の間にしかないため）
for i in range(-202,203):
    grids[(202, i)] = '#'
    grids[(-202, i)] = '#'
    grids[(i, 202)] = '#'
    grids[(i, -202)] = '#'

Q = deque()
# x座標、y座標、移動カウントのタプルを格納
Q.append((0,0,0))
grids[(0,0)] = 'DONE'

while len(Q) > 0:
    now = Q.popleft()
    x = now[0]
    y = now[1]
    for next in [(x+1,y+1), (x,y+1),(x-1,y+1), (x+1,y), (x-1,y), (x, y-1)]:
        if grids[next] == '.':
            Q.append(next + (now[2] + 1,))
            grids[next] = 'DONE'
        if next == (gx, gy):
            print(now[2] + 1)
            exit()
print(-1)


"""
blocks = []
for _ in range(N):
    blocks.append(list(map(int, input().split())))

# 外壁（ゴールのx座標y座標ともに-200~200の間にしかないため）
for i in range(-202,203):
    blocks.append([202,i])
    blocks.append([-202,i])
    blocks.append([i, 202])
    blocks.append([i, -202])
    
dist_dict = {}

Q = deque()    
sx, sy = [0,0]
Q.append([sx, sy])
dist_dict[str(sx) + "," + str(sy)] = 0

while len(Q) > 0:
    now = Q.popleft()
    x = now[0]
    y = now[1]
    for next in [[x+1,y+1], [x,y+1],[x-1,y+1], [x+1,y], [x-1,y], [x, y-1]]:
        k = str(next[0]) + "," + str(next[1])
        if not (next in blocks) and not (k in dist_dict):
            Q.append(next)
            dist_dict[k] = dist_dict[str(x) + "," + str(y)] + 1
            if next == [gx, gy]:
                print(dist_dict[k])
                exit()

print(-1)
"""
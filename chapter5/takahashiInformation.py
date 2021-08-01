# ABC88 C https://atcoder.jp/contests/abc088
c = [list(map(int,input().split())) for _ in range(3)]

# 列方向での確認
for i in range(0, len(c[0])):
    next_ind = i + 1
    if i == len(c[0])-1:
        next_ind = 0
    x = c[0][i] - c[0][next_ind]
    y = c[1][i] - c[1][next_ind]
    z = c[2][i] - c[2][next_ind]
    
    if x == y == z:
        continue
    else:
        print("No")
        exit()
    
# 行方向での確認
for i in range(0, len(c)):
    next_ind = i + 1
    if i == len(c)-1:
        next_ind = 0
    x = c[i][0] - c[next_ind][0]
    y = c[i][1] - c[next_ind][1]
    z = c[i][2] - c[next_ind][2]
    
    if x == y == z:
        continue
    else:
        print("No")
        exit()

print("Yes")
        

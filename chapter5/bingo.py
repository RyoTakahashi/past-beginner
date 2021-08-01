# ABC157 B (https://atcoder.jp/contests/abc157/tasks/abc157_b)
a = [list(map(int,input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

# 全探索する
result = []
for i in range(0,len(a)):
    result_i = []
    for j in range(0,len(a[i])):
        if a[i][j] in b:
            result_i.append(1)
        else:
            result_i.append(0)
    # 横ビンゴはこのタイミングで判定する
    if sum(result_i) == len(result_i):
        print("Yes")
        exit()
        
    result.append(result_i)

# 縦,斜めビンゴ判定
if (result[1][1] == 1) and (result[0][0] == 1) and (result[2][2] == 1):
    print("Yes")
    exit()
elif (result[1][1] == 1) and (result[0][2] == 1) and (result[2][0] == 1):
    print("Yes")
    exit()
else:
    col_sum = [0 for _ in range(0,len(result))]
    for result_i in result:
        col_sum = [x + y for (x, y) in zip(col_sum, result_i)]

    if max(col_sum) == len(result):
        print("Yes")
        exit()

print("No")




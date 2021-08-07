# 第一回PAST H問題 https://atcoder.jp/contests/past201912-open/tasks/past201912_h
import math
N = int(input())
c_lst = list(map(int, input().split()))
Q = int(input())

# セット販売のカード種類数
odd_num = math.ceil(N/2)

sold_cnt = 0
# セット販売で売ったカードの枚数（1枚あたり）
odd_sold_cnt = 0
# 全種類販売で売ったカードの枚数（1枚あたり）
all_sold_cnt = 0

min_odd = pow(10,9)
min_even = pow(10,9)

for i in range(0, N):
    if i % 2 == 0:
        min_odd = min(c_lst[i], min_odd)
    else:
        min_even = min(c_lst[i], min_even)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        target = q[1] - 1 
        sale_num = q[2]
        if target % 2 == 0:
            # セット販売対象のカード枚数
            c_num = c_lst[target] - odd_sold_cnt - all_sold_cnt
        else:
            # セット販売対象外のカード枚数
            c_num = c_lst[target] - all_sold_cnt
            
        if c_num >= sale_num:
            c_lst[target] -= sale_num
            sold_cnt += sale_num
            # 最小値の更新
            if target % 2 == 0:
                min_odd = min(c_lst[target], min_odd)
            else:
                min_even = min(c_lst[target], min_even)
    elif q[0] == 2:
        sale_num = q[1]

        if (min_odd - odd_sold_cnt - all_sold_cnt) >= sale_num:
            odd_sold_cnt += sale_num
    else:
        sale_num = q[1]
        if min(min_odd - odd_sold_cnt - all_sold_cnt, min_even - all_sold_cnt) >= sale_num:
            all_sold_cnt += sale_num
            
sold_cnt += (odd_sold_cnt * odd_num) + (all_sold_cnt * N)
print(sold_cnt)
            
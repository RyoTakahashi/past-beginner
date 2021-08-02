# ARC 46 A (https://atcoder.jp/contests/arc046/tasks/arc046_a)
n = int(input())

len_cnt = 1
num = 1
for _ in range(n-1):
    if num == 9:
        len_cnt += 1
        num = 1
    else:
        num += 1

print(str(num) * len_cnt)
    

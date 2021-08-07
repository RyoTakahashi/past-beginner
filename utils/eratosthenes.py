import math

def eratosthenes(n):
    prime_lst = []
    num_list=[i for i in range(2, n+1)] # 2以上n以下の整数を並べる
    limit = math.sqrt(n) #探索範囲の上限
    while True:
        if limit <= num_list[0]:
            return prime_lst + num_list
        # num_lst[0]を追加する
        prime_lst.append(num_list[0])
        # num_lst[0]の倍数でないものだけを残す=素数にはなりえないため
        num_list = [e for e in num_list if e % num_list[0] != 0] 
    
# 1000までの素数リスト
max_v = 1000
print(eratosthenes(max_v))
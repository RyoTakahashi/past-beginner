# ABC165 A (https://atcoder.jp/contests/abc165/tasks/abc165_a)
#"""Bruteforce solution
k = int(input())
a, b = map(int, input().split())

for num in range(a, b+1):
    if num % k == 0:
        print("OK")
        exit()

print("NG")

#"""

"""mathematical solution
k = int(input())
a, b = map(int, input().split())

if int(a / k) < int(b / k):
    print("OK")
elif a % k == 0:
    print("OK")
else:
    print("NG")

"""
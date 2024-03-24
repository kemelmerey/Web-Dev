x = int(input())
cnt=0
for i in range(1, x+1):
    if x % i == 0:
        cnt+=cnt
        print(i, end=" ")
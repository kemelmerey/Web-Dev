a = int(input())
arr = list(map(int, input().strip().split()))
arr = [i for i in arr if i % 2 == 0]

for i in arr:
    print(i, end = " ")
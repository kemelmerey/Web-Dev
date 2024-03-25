a = int(input())
arr = list(map(int, input().strip().split()))
arr = [i for i in arr if i > 0]

print(len(arr))
    
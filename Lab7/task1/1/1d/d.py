a = int(input())
arr = list(map(int, input().strip().split()))
cnt = 0
arr = [i for i in range(len(arr)-1) if arr[i] < arr[i+1]]
print(len(arr))
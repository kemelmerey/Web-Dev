a = int(input())
arr = list(map(int, input().strip().split()))

arr = [i for i in range(len(arr)-1) if (arr[i] > 0 and arr[i+1] > 0) or (arr[i] < 0 and arr[i+1] < 0) ]
if len(arr)!=0:
    print("YES")
else: print("NO")
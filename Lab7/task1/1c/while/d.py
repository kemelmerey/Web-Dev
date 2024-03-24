n = int(input())
i = 0

while i < n:
    if pow(2, i) == n:
        print("YES")
        break
    if pow(2, i) < n:
        pass
    if pow(2, i) > n:
        print("NO")
        break
    i += 1
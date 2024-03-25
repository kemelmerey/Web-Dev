n = int(input())
i = 0
while i <= n:
    if pow(2, i) <= n:
        print(pow(2, i))
    else:
        break
    i += 1
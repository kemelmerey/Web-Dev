x = int(input())
e = 0

for i in range(1, x+1):
    if x % i == 0:
        e += 1

print(e)
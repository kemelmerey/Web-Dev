def xor(x, y):
    if x == y:
        return 0
    elif x == 1 or y == 1:
        return 1
    
x, y = map(int, input().split())

print(xor(x, y))
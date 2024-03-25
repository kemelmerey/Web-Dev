def find_min(a, b, c, d):
    return min(a, b, c, d)

a, b, c, d = map(int, input().split())

res = find_min(a, b, c, d)
print(res)
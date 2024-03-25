a = input()
cnt = 0

for i in range(len(a)):
    cnt += int(a[i]) * pow(2, len(a)-i-1)

print(cnt)
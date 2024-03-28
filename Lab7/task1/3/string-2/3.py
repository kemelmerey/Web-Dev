def count_hi(str):
    n = len(str)
    cnt = 0
    for i in range(n-1):
        if str[i:i+2] == 'hi':
        cnt += 1
    
    return cnt
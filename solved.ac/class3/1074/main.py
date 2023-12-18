# https://www.acmicpc.net/problem/1074

N, r, c = map(int, input().split())

def divide_and_conquer(N, R, C, offset):
    if R == r and C == c:
        return offset
    elif N < 1:
        return -1
    else:
        unit = 2 ** (N-1) 
        diff = ((2 ** N) * (2 ** N)) // 4
        result = divide_and_conquer(N-1, R, C, offset) # 1사분면
        if result != -1: return result

        result = divide_and_conquer(N-1, R, C + unit, offset + (diff * 1)) # 2사분면
        if result != -1: return result

        result = divide_and_conquer(N-1, R + unit, C, offset + (diff * 2)) # 3사분면
        if result != -1: return result

        result = divide_and_conquer(N-1, R + unit, C + unit, offset + (diff * 3)) # 4사분면
        if result != -1: return result
        return -1
        

print(divide_and_conquer(N, 0, 0, 0))
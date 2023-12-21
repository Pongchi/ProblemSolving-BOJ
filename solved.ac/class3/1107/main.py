# https://www.acmicpc.net/problem/1107

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
brokens = [False] * 10

if M > 0:
    for n in map(int, input().split()):
        brokens[n] = True

def inputChannelCount():
    def canInput(channel):
        if channel == 0:
            if brokens[0]: return False
            else: return True

        while channel:
            if brokens[channel % 10]:
                return False
            channel //= 10
        return True
    # Start inputChannelCount
    result = set()
    for i in range(N+10):
        for sign in [1, -1]:
            channel = N + (sign*i)
            if channel >= 0 and canInput(channel):
                result.add(len(str(channel)) + i)
    return min(result) if result else float('inf')

print(min(inputChannelCount(), abs(100 - N)))
"""program to find product of digits"""
N = int(input())
COUNT = 0
PROD = 1
REM = 0
TEMP = N
if TEMP == 0:
    print(0)
if TEMP < 0:
    TEMP = -(TEMP)
while TEMP > 0:
    REM = TEMP % 10
    PROD = PROD * REM
    TEMP = TEMP // 10
if N < 0:
    print(-PROD)
if N > 0:
    print(PROD)

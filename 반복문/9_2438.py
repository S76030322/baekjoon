# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별N개를 찍는 문제

import sys

N = int(sys.stdin.readline())

print("\n".join(['*' * i for i in range(1,N+1)]))
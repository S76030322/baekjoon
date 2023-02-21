# 문제
# 빠른 A+B

# 입력
# 첫 줄에 테스트케이스 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수A와 B가 주어진다. A와 B는 1이상, 1,000이하이다.

import sys

T = int(sys.stdin.readline())
print(*[sum(map(int,sys.stdin.readline().split())) for _ in range(T)])
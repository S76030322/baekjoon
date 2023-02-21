# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에는 A와 B가 주어진다.(0<A, B<10)

import sys

T = int(sys.stdin.readline())

print('\n'.join([f"Case #{i}: {a} + {b} = {a+b}" for i, (a, b) in enumerate([map(int,sys.stdin.readline().split()) for _ in range(T)], 1)]))

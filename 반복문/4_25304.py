# 문제
# 영수증을 보면서 정확하게 계산된 거이 맞는지 확인해보려 함

# 입력
# 첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
# 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.

X = int(input())
N = int(input())
total_cost = sum([price * quantity for price, quantity in [map(int, input().split()) for _ in range(N)]])
print("Yes" if total_cost == X else "No")
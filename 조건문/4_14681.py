# 문제
# 흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다.
# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.

# x,y = map(int,input().split())
# print("3421"[x>0::2][y>0])

print("3421"[int(input())>0::2][int(input())>0])
# 문제
# n이 주어졌을 때, 1 부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())
print(sum([i for i in range(1,n+1)]))
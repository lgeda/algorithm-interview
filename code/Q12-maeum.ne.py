# 주식을 사고팔기 가장 좋은 시점
# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라
# 입력: [7, 1, 5,3 , 6, 4]
# 출력: 6

import sys

min_price = sys.maxsize
profit = 0
input = [7, 1, 5, 3, 6, 4]
for price in input:
    min_price = min(min_price, price)
    profit = max(price - min_price, profit)

print(profit)

t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    
    max_price = 0  # 최대 가격
    profit = 0  # 이익

    for i in range(n-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            profit += max_price - prices[i]
    
    print(profit)
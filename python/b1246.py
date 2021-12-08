N, M = map(int, input().split())
customer = [int(input()) for _ in range(M)]
customer.sort(reverse=True)

max_profit = 0
price = 0
for i in range(min(N, M)):
    profit = (i + 1) * customer[i]
    if max_profit < profit:
        max_profit = profit
        price = customer[i]

print(price, max_profit)
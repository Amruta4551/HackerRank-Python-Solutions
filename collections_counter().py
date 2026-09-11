from collections import Counter

n = int(input())
shoes = list(map(int, input().split()))
customers = int(input())

count = Counter(shoes)
earnings = 0

for _ in range(customers):
    size, price = map(int, input().split())
    if count[size] > 0:
        earnings += price
        count[size] -= 1

print(earnings)

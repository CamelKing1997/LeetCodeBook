def maxProfit(prices: [int]) -> int:
    cost = float("+inf")
    out = 0
    for price in prices:
        if price < cost:
            cost = price
        if price-cost > out:
            out = price - cost
    return out

print(maxProfit([7,1,5,3,6,4]))
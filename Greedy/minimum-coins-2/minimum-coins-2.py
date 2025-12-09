def min_coins(coins, amount):
    coins.sort(reverse=True)
    res = 0
    for coin in coins:
        res += amount // coin
        amount %= coin
    return res

# Example usage
coins = [25,10,5,1]
amount = 63
print("Output:", min_coins(coins, amount))

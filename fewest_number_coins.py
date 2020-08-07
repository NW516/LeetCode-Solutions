# Given an integer number of cents, print out a breakdown
# of pennies, nickels, dimes and quarters, using the fewest
# number of coins

import sys

amt = int(sys.argv[1])

coins = [["quarter", 25],["dime", 10],["nickel",5],["penny",1]]
coins_used = []

for c in (coins) :
    this_coin = [c[0]]
    ctr = 0
    while (amt-c[1] > 0) :
        ctr = ctr + 1
        amt = amt - c[1]
    this_coin.append(ctr)
    coins_used.append(this_coin)
print(coins_used)

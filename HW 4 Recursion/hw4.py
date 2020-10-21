import random

'''
Task 1: Write the following function: change(amount, coins)
The recursive approach to this problem considers two branches, as each coin will either be used
in the amount (possibly multiple times) or not used at all.
If at some point, it becomes clear that the current amount cannot be made from the coins list, the function should return a number that represents there is no possible way to create the amount. This is achieved by float(‘‘inf’’), which works like the largest number.
You can assume that amount is always an integer, and coins is always an array of positive integers. Your function should return a single integer, which is the smallest amount of coins from coins required to sum up to amount.
Here are some examples you can check your program against to make sure they work:
•change(6, [1, 3]) == 2,asthe3+3=6isthefastestwaytomake6.
• change(313, [7, 24, 42]) == 10, as case 1(7) + 4(24) +5(42) does indeed add up to 313.
• change(13, [8, 3, 9, 6]) == float(‘‘inf’’), as there is no combination of the coins that add up to 13.
'''
def change(amount, coins):
    if amount < 0:
        return float("inf")
    if len(coins) == 0 and amount > 0:
        return float("inf")
    if len(coins) == 0 and amount == 0:
        return 0
    return min(change(amount-coins[0], coins) + 1, change(amount, coins[1:]))

'''
Task 2: Use a lambda function to generate a random list of coins of a certain length: currency(length)
Example:
• currency(5) = [7, 4, 8, 6, 2] (or any other length-5 list of numbers with no duplicates)
'''
def currency(length):
    return list(map(lambda x: random.randrange(5*x, 5*x+5),range(length)))


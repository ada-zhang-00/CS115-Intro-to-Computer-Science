# Import reduce from the functools package
from functools import reduce

#######################################################################################
# Task 1: Use reduce to determine if all elements in a boolean list are true
def all_true(lst):
    return reduce(lambda x,y: x and y,lst)
print(all_true([True,True,False,True]))
print(all_true([True,True,True,True]))
print(all_true([False,False,False,False]))

#######################################################################################
# Task 1.1: Use reduce to determine if AT LEAST one element in a boolean list is true
# Hint: Should be very similar to the above function
def one_true(lst):
    return reduce(lambda x,y: x or y,lst)

print(one_true([True,True,True,True]))
print(one_true([False,False,False,False]))
print(one_true([False,False,True,False]))

#######################################################################################
# Task 2: Use map and reduce to return how many elements are True in a boolean list
def count_true(lst):
    return reduce(lambda x,y: x+y, map(lambda x: int(x), lst))

''' True = 1, False = 0 in python
    5/True => 5
'''

'''
definitions:
        map( function(a) , iterable):
            function for map only takes on argument
            applies function to each member of iterable

            map(lambda x: int(x), lst)
            converts lst to list of integers

        reduce( function (a, b)  , itearble):
            function for reduct takes two arguments
            applies function to each member of iterable, using previous iteration's output as next input
            [1,2,3,4,5,6,7,8]

            reduce(lambda x,y: x+y, list of integers)
                                    [1,2,3,4,5,6,7,8]
            1+2=3 (3 becomes nxt x) [3,4,5,6,7,8]
            3+3=6 (6 becomes nxt x) [4,5,6,7,8]
            ...
            
'''

print(count_true([True,True,True,True]))
print(count_true([False,False,False,False]))
print(count_true([False,False,True,False]))

# This function is provided for you
# Gets a list of strings through the command line
# Input is accepted line-by-line
def getInput():
    lst = []
    txt = input()

    while(len(txt) != 0):
        lst.append(txt)
        txt = input()

    return lst
'''
txt = input
lst.append(txt) = puts the txt in lst if the length is not zero

getinput returns a list of strings
'''

# Task 3: Get the longest string in the list using map and reduce, and print it out
# 'strings' is a list of input strings e.g. [ 'hello', 'world' ]
# Hint: The 'map' part of your program should take a string s into a length-2 list [len(s), s].

def getLongestString():
    return (reduce(lambda x,y: x if len(x)>len(y) else y, getInput()))
'''
getinput is a list of strings

lambda x,y: x if len(x)>len(y) else y = look to see if the first thing on list is greater than the second thing,
    if so return first if not retunr second, then move one with second/first and third
example:
getInput = [apple, phone, chocolate,omar]
apple!>phone .... return phone
phone!>chocolate...return chocolate
chocolate>omar... return chocolate
'''

print(getLongestString())


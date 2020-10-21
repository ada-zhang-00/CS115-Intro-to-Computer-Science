# The binary format you'll be working with for this assignment is called R2L,
# as it is a right-to-left representation.
####################################################################################
## Ex: 8 in decimal is 1000 in standard binary (2^3),
## and represented as a list [0, 0, 0, 1] in our R2L representation.
####################################################################################

# Notice that this makes it very easy to work with binary,
# by using num[0] to grab the least significant bit (2^0)!
#
# Please fill out the following 4 functions below using recursion, as specified.

# Given an integer x >= 0, convert it to the R2L binary format.
# Take note that both [] and [0] are used to represent 0 in R2L
def decimalToBinary(x):
    return list(map(int, bin(int(x))[2:][::-1]))

    #bin(int) =def decimalToBinary(n)
    #binary is denoted by 0bXXXX
    #hexadecimal is denoted by 0xXXXX
    
    

# Given an R2L formatted number, return the integer it is equivalent to.
# The function should function with both [] and [0] returning 0.
def binaryToDecimal(num):
   return int(''.join(map(str, num))[::-1], 2)


# Given an R2L formatted number, return an R2L equivalent to num + 1
# If you need to increase the length, do so. Again, watch out for 0
def incrementBinary(num):
   return decimalToBinary(binaryToDecimal(num)+1)

# Given 2 R2L numbers, return their sum.
## You MUST implement recursively the algorithm for bit-by-bit addition as taught in class,
## you may NOT do something like decimalToBinary( binaryToDecimal(num1) + binaryToDecimal(num2) ).
# Make sure to figure out what to do when num1 and num2 aren't of the same length!
# (and be sure you can add [] and [0])
## Tip: Try this on paper before typing it up
def addBinary(num1, num2):
    return list(map(int, (add_bitwise(''.join(map(str, num1))[::-1], ''.join(map(str, num2))[::-1]))[::-1]))

def add_bitwise(num1,num2):
    if num1 == "" and num2 == "":
        return ""
    elif num1 == "":
       return num2
    elif num2 == "":
       return num1
    else:
        sum_rest = add_bitwise(num1[:-1], num2[:-1])
        if num1[-1] == "1" and num2[-1] == "0":
            return sum_rest + "1"
        elif num1[-1] == "0" and num2[-1] == "1":
            return sum_rest + "1"
        elif num1[-1] == "0" and num2[-1] == "0":
            return sum_rest + "0"
        elif num1 == "1" and num2 == "1": 
            return sum_rest + "10"
        else:
            return add_bitwise(sum_rest, "1") + "0"   


from math import floor

######################################################################
# Task 1: Given an 8-digit decimal number representing the date,
#         calculate the day of the week
# Input: 8-digit decimal number in the format of YYYYMMDD
# Saturday: 0, Sunday: 1... Friday: 6  
# Hint: Look at Zeller's congruence.
#       The floor() function may be helpful. (Ex: floor(5.5) = 5)

def getWeekday(timestamp):
    y = timestamp//10000
    c = y%100
    z = y//100
    m_date = timestamp%10000
    m = m_date//100
    d = m_date%100
    timestamp = (d + ((26 * (m + 1)) // (10)) + c + ((c) // (4)) + ((z) // (4)) + (5 * z)) % 7

    if timestamp == 0:
        print('Day of the week is Saturday')
    elif timestamp == 1:
        print('Day of the week is Sunday')
    elif timestamp == 2:
        print('Day of the week is Monday')
    elif timestamp == 3:
        print('Day of the week is Tuesday')
    elif timestamp == 4:
        print('Day of the week is Wednesday')
    elif timestamp == 5:
        print('Day of the week is Thursday')
    elif timestamp == 6:
        print('Day of the week is Friday')

        
######################################################################
# Task 2: For this task, you will create an encoder and decoder
#         for a Caesar cipher using the map function.
# You may find this website helpful:
# https://cryptii.com/pipes/caesar-cipher

######################################################################
# This provided helper function may be useful
# Input: List of ASCII values (Ex: [72, 69, 76, 76, 79])
# Output: String (Ex. 'HELLO')     ('H   E   L   L   O')
def asciiToString(asciiList):
    return ''.join(map(chr, asciiList))

######################################################################
# Encoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. HELLO WORLD, 3)
# Output: An encoded string            (Ex. KHOOR ZRUOG)
# Hint: The ord() function converts single-character strings to ASCII

def caesarEncoder(strin, shiftval): 
    return ''.join(list(map(lambda x: chr(65+((ord(x)-65+shiftval%26)%26)) if x != ' ' else ' ', strin)))


    
    
######################################################################
# Decoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. KHOOR ZRUOG, 3)
# Output: A decoded string             (Ex. HELLO WORLD)
# Hint: The chr() function converts ASCII to a single-character string
    
def caesarDecoder(strin, shiftval):
    return ''.join(list(map(lambda x: chr(65+((ord(x)-65-shiftval%26)%26)) if x != ' ' else ' ', strin)))


print(caesarDecoder('KHOOR ZRUOG', 29))

'''
dotProduct(L, K) should output the dot product of the lists L and K. Recall that the dot product of two vectors or lists is the sum of the products of the elements in the same position in the two vectors.
You may assume that the two lists are of equal length. If they are of different lengths, it's up to you what result is returned. If these two lists are both empty, dot should output 0.0. Assume that
the input lists contain only numeric values.
>>> dotProduct([5,3], [6,4]) <-- Note that 5*6 + 3*4 = 42
42
'''
def dotProduct(L,K):
    if len(L) == 0 or len(K) == 0:
        return 0
    return L[0]*K[0]+dotProduct(L[1:],K[1:])

'''
expand(S) should take a string S as input and should return a list of the characters (each of
which is a string of length 1) in that string. For example:
>>> expand("spam")
['s', 'p', 'a', 'm']
>>> expand("")
[]
'''
def expand(s):
    if len(s) == 0:
        return []
    else:
        lr = [s[0]]
        return lr + expand(s[1:])

'''
deepMember(e, L) takes in an element e and a sequence L where by "sequence" we mean a list. deepMember analyzes the list, and returns True if e is in L, or in any sublist of L, or sublist of a sublist, etc.
>>> deepMember(42, [ 55, 77, 42, 12, 42, 100 ])
True
>>> deepMember(42, range(0,100))
True
>>> deepMember('hi', [ 'hello', 42, True ])
False
>>> deepMember('hi', [ [‘hello’, ‘there’], [‘general’, ‘kenobi’]])
False
>>> deepMember('i', ['team'])
False
>>> deepMember(3, [1, [2, [3, [4]]]])
True
>>> deepMember(23, [ 2, 3, [4, 5, 6] , [20, 21, [22, 23]] , 42 ])
True
'''
def deepMember(e, L):
    if len(L) == 0:
        return False
    if e == L[0]:
        return True
    if type(L[0]) == list:
        return (deepMember(e, L[0]) or deepMember(e, L[1:]))
    else:
        return deepMember(e, L[1:])
    
'''
removeAll(e, L) takes in an element e and a list L. Then, removeAll should return another list that is identical to L except that all elements identical to e have been removed. Notice that e has to be a top-level element to be removed, as the examples illustrate:
>>> removeAll(42, [ 55, 77, 42, 11, 42, 88 ])
[ 55, 77, 11, 88 ]
>>> removeAll(42, [ 55, [77, 42], [11, 42], 88 ]) <-- NOTICE HERE THAT 42 IS NOT TOP-LEVEL - IT'S "HIDING" DEEP INSIDE OTHER LISTS AND IS NOT ITSELF AN ELEMENT OF THE LIST L
[ 55, [77, 42], [11, 42], 88 ]
>>> removeAll([77, 42], [ 55, [77, 42], [11, 42], 88 ]) # <-- NOTICE HERE THAT THE LIST [77, 42] IS TOP-LEVEL; IT'S AN ELEMENT OF THE LIST L.
[ 55, [11, 42], 88 ]
'''
def removeAll(e, L):
    if len(L) == 0:
        return L
    if e != L[0]:
        return [L[0]] + removeAll(e, L[1:])
    else:
        return removeAll(e, L[1:])

'''
deepReverse(L) takes as input a list of elements where some of those elements may be lists themselves. deepReverse returns the reversal of the list where, additionally, any element that is a list is also deepReversed. Here are some examples:
>>> deepReverse([1, 2, 3])
[3, 2, 1]
>>> deepReverse([1, [2, 3], 4])
[4, [3, 2], 1]
>>> deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]])
[[[8, [7, 6], 5], [4, 3], 2], 1]
'''
def deepReverse(L):
    if L == []:
        return L
    elif type(L) != list:
        return L
    else:
        return deepReverse(L[1:]) + [deepReverse(L[0])]


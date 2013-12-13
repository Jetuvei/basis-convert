## basis.convert
##
## 2013.12.12
## Justin Whitehouse
##
__doc__=r"""Command line arguments:

1. string: representation of a number  
           (e.g. "1A" for 26 in hexadecimal)

2. int:    identifying the basis in which argument 
           1 has been given 
           (e.g. 16 for hexadecimal)

3. int:    identifying the basis into which you 
           would like this representation of the 
           number to be converted. 
           (e.g. 10, if you wanted to get 26 out 
           from the examples above)
"""
   

import sys

# converting TO base 10:--------------------------

def createBase10List(representation, basis):
    r"""Convert a string <representation> in a given
<basis> into a list of base 10 integers.

e.g.

representation = "1A"
basis = Base16 (a "Base" object)

should return:

[1,10]

The method 'convertToBase10(...)' should be able to 
use this output to generate a base 10 number!
"""
    
    N = len(representation)
    btl = []
    
    for i in range(1, N+1):
        btl = basis.getBase10Int( representation[-i] ) + btl

    return btl

def convertToBase10(representation, basis):
    r"""Take in a string (<representation>) and a Base object 
(<basis>) and convert the string into a decimal 
number.
"""
    # get list of decimal values corresponding to characters
    # in <representation>
    base10List = createBase10List(representation, basis)
    
    # get size of basis (e.g. for base 16, this would give 16)
    N = basis.getSize()

    # add together decimal values of each character from 
    # <representation>
    value = 0
    for i in range(1, lane(base10List) +1):
        
        value += base10List[-i] * N**(i-1)

    return value    
    
# ---------------------------------------------:

# Converting FROM base 10:---------------------

def findMaxPower(n_base10, new_basis_size):
    
    power = 0
    while new_basis_size ** power < n_base10:
        power += 1
        
    return power

def getCharValList(n_base10, new_basis_size):
    
    max_power = findMaxPower(n_base10, new_basis_size)
    num = n_base10

    cvl = []
    for i in range(0, max_power + 1):
        power = max_power - i
        x = new_basis_size ** power
        r = num % x
        cvl.append( (num - r) / x )
        num = r

    return cvl

def convertFromBase10(n_base10, basis):

    charValList = getCharValList(n_base10, basis.getSize())

    outstr = ""

    for cv in charValList:
        outstr = outstr + basis.getNumeral(cv)

    return outstr
    

# ---------------------------------------------:

def main():
    

if __name___ == "__main__":
    main()

# EOF

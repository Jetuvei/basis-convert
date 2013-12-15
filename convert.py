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
import bases

# KNOWN BASES

KNOWN_BASES = {2: bases.BASE2,
               10: bases.BASE10,
               16: bases.BASE16
               }

KNOWN_BASES_MESSAGE = "Known bases:\n"
for basis in KNOWN_BASES:
    KNOWN_BASES_MESSAGE += str(basis) + "\n"

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
        btl = [ basis.getBase10Int( representation[-i] ) ] + btl

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
    for i in range(1, len(base10List) +1):
        
        value += base10List[-i] * N**(i-1)

    return value # returns int
    
# ---------------------------------------------:

# Converting FROM base 10:---------------------

def findMaxPower(n_base10, new_basis_size):
    r"""Find largest power of the new basis size that is less 
than the base 10 number. For example:

12 in base 2 is 1*2^3 + 1*2^2 + 0*2^1 + 0*2^0

The largest power is 3, and this should be returned.
"""

    # check that we've been given an int for the basis size
    if type(new_basis_size) != int:
        raise TypeError("Expected type int, found " + str(type(new_basis_size)))
    else:
        pass

    # make sure we have an integer value of n_base10:
    n_base10 = int(n_base10)

    if n_base10 == 0:
        power = None
    else:
        power = 0
        while new_basis_size ** (power+1) <= n_base10:
            power += 1
        
    return power # must return int

def getCharValList(n_base10, new_basis_size):
    r"""Return a list of integers, where the integers are
the multiple of the corresponding power of the basis size.

e.g. 175 in base 16 should return [10,15]
"""
    
    max_power = findMaxPower(n_base10, new_basis_size)
    num = int(n_base10) # make sure this is actually an integer

    cvl = []
    for i in range(0, max_power + 1):
        power = max_power - i
        x = new_basis_size ** power
        r = num % x
        cvl.append( (num - r) / x )
        num = r

    return cvl

def convertFromBase10(n_base10, basis):
    r"""Should return a representation string of the base
10 integer in the new basis.

e.g. 175 in base 16 should return "AF"

this function uses getCharValList(...)
"""

    charValList = getCharValList(n_base10, basis.getSize())

    outstr = ""

    for cv in charValList:
        outstr = outstr + basis.getNumeral(cv)

    return outstr
    

# ---------------------------------------------:

def main_case_1(number, basis_to):
    """CASE 1: the 'from' basis is 10, the 'to' basis is not 10."""
    return convertFromBase10(number, KNOWN_BASES[basis_to])
    
def main_case_2(number, basis_from):
    """CASE 2: the 'to' basis is 10, the 'from' basis is not 10"""
    return convertToBase10(number, KNOWN_BASES[basis_from])

def main_case_3(number, basis_from, basis_to):
    """CASE 3: neither the 'to' nor the 'from' bases are 10"""
    return main_case_1( main_case_2( number, basis_from ), basis_to )
                              

# main

def main(number, basis_from, basis_to, is_test):
    """The main function should enable us to take three arguments from the command line:

1. number (string representation)
2. basis to convert FROM
3. basis to convert TO

EXIT CODES:

1. one or more unknown/unrecognised bases supplied in arguments

"""
    result = None
    unknown_bases = False

    # if basis_from == basis_to, don't need to do anything:
    if basis_from == basis_to:
        result = number
    
    # otherwise
    else:
        
        # first, check that the given bases are ones we know about
        # (remember: everything from the command line is a string)
        for basis in [basis_from, basis_to]:
            if int(basis) not in KNOWN_BASES:
                unknown_bases = True
                print "Unknown basis:" + str(basis)
                
        if unknown_bases:
            print KNOWN_BASES_MESSAGE
            sys.exit(1)

        # otherwise, if we recognise BOTH of the bases: carry on
        else:

            if basis_from == 10:
                
                result = main_case_1(number, basis_to)

            elif basis_to == 10:
                
                result = main_case_2(number, basis_from)

            else:
                
                result = main_case_3(number, basis_from, basis_to)

    if is_test:
        return result
    else:
        print result
        sys.exit(0)
            

# TESTS

def test_findMaxPower_1():
    assert findMaxPower(16,2) == 4

def test_findMaxPower_2():
    assert findMaxPower(15,2) == 3

def test_createBase10List_1():
    assert createBase10List("1A", bases.BASE16) == [1,10]

def test_convertFromBase10_1():
    assert convertFromBase10(8,bases.BASE2) == "1000"

def test_convertToBase10_1():
    assert convertToBase10("AF", bases.BASE16) == 175

def test_getCharValList_1():
    assert getCharValList(175, bases.BASE16.getSize()) == [10,15]

def test_main_case_1_1():
    assert main_case_1(8,2) == "1000"

def test_main_case_1_2():
    assert main_case_1("8",2) == "1000"

def test_main_case_2_1():
    assert main_case_2("1000",2) == 8

def test_main_1():
    """ FF -> 255 -> 11111111 """
    assert main("FF", 16, 2, True) == "11111111"

# run from cmd line    

if __name__ == "__main__":
    n = sys.argv[1]
    b_from = int(sys.argv[2])
    b_to = int(sys.argv[3])
    main(n, b_from, b_to, False) # False: not a test

# EOF

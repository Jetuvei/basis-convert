
"""Basis class for use with 'convert.py'
"""

class Basis:
    r"""Class for defining a basis for converting  
    integers between counting bases.

Properties:

_SIZE       int        size of the basis. (e.g. 10 for base 10)

_NUMERALS   dictionary:

            key:    int    integer value less than SIZE
            value:  str    character to use when printing 
                           this number (e.g. 10:"A" for base 16)

"""
    def __init__(self, s, n):
        try:
            assert s == len(n)
        except AssertionError:
            raise ValueError("Basis size 's' does not equal the size of the numerals dictionary 'n'")
        _SIZE = s
        _NUMERALS = n

    def getSize(self):
        return _SIZE

    def getNumeral(self, n):
        r"""return numeral corresponding to the representation
of the integer n in this representation. 

n must be >= 0 and < _SIZE

e.g. base 2:   0 -> "0"
     base 10:  9 -> "9"
     base 16: 11 -> "B"
"""
        return _NUMERALS[n]

    def getBase10Int(self, c):
        r"""return base 10 intger corresponding to the 
character c from the numerals/representation in this 
basis.
"""
        value = None
        for n in _NUMERALS:
            if _NUMERALS[n] == c:
                value = n
            else:
                pass
        return value            

# base 2 / binary

class Base2(Base):
    r"""Class for base 2, AKA binary
"""

    def __init__(self):
        _SIZE = 2
        _NUMERALS = {0:"0",
                     1:"1"
                     }

# base 10 / decimal

class Base10(Base):
    r"""Class for base 10. Basically pointless, as
this whole module/package uses base 10 as its working
basis.
"""

    def __init__(self):
        _SIZE = 10
        _NUMERALS = {0:"0",
                     1:"1",
                     2:"2",
                     3:"3",
                     4:"4",
                     5:"5",
                     6:"6",
                     7:"7",
                     8:"8",
                     9:"9"
                     }

# base 16 / hexadecimal

class Base16(Base):
    r"""
"""

    def __init__(self):
        _SIZE = 16
        _NUMERALS =  {0:"0",
                      1:"1",
                      2:"2",
                      3:"3",
                      4:"4",
                      5:"5",
                      6:"6",
                      7:"7",
                      8:"8",
                      9:"9",
                      10:"A",
                      11:"B",
                      12:"C",
                      13:"D",
                      14:"E",
                      15:"F"
                      }


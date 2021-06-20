import re

class Convert():

    roman = {
        'units':     ['I','II','III','IV','V','VI','VII','VIII','IX'],
        'tens':      ['X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
        'hundreds':  ['C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
        'thousands': ['M','MM','MMM']
    }

    arabic = {
        'units':     [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'tens':      [10, 20, 30, 40, 50, 60, 70, 80, 90],
        'hundreds':  [100, 200, 300, 400, 500, 600, 700, 800, 900],
        'thousands': [1000, 2000, 3000]
    }

    def __isValidArabicNumeral(self, number):
        if number is None:
            raise ValueError
        if not isinstance(number, int):
            raise ValueError
        if number <= 0:
            raise ValueError
        if number > 3999:
            raise ValueError
        return True
    
    def __isValidRomanNumeral(self, number):
        p = re.compile('[IVXLCDMivxlcdm]+')
        if p.match(number):
            return True
        return False
    
    def __parseRomanNumeral(self, number):
        p = re.compile('^(M{0,4})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
        return p.findall(number)

    def __encode(self, value, index):
        # Special case zero is nothing
        if (int(value) == 0):
            return ''

        if index == 3:
            return self.roman['thousands'][int(value)-1]
        elif index == 2:
            return self.roman['hundreds'][int(value)-1]
        elif index == 1:
            return self.roman['tens'][int(value)-1]
        else:
            return self.roman['units'][int(value)-1]

    def __decode(self, value, index):
        if not value:
            return 0
        
        if index == 3: # Matches units
            return self.arabic['units'][self.roman['units'].index(value)]
        elif index == 2: # Matches tens
            return self.arabic['tens'][self.roman['tens'].index(value)]
        elif index == 1: # Matches hundreds
            return self.arabic['hundreds'][self.roman['hundreds'].index(value)]
        else: # Matches thousands
            return self.arabic['thousands'][self.roman['thousands'].index(value)]

    def toRoman(self, number=None):
        if self.__isValidArabicNumeral(number):
            original = [x for x in str(number)]
            original.reverse()
            encoded = [self.__encode(x, i) for i, x in enumerate(original)]
            encoded.reverse()
            return ''.join(encoded)
        else:
            raise ValueError
    
    def toArabic(self, number=None):
        if self.__isValidRomanNumeral(number.upper()):
            parsed = list(self.__parseRomanNumeral(number.upper())[0])
            decoded = [self.__decode(x, i) for i, x in enumerate(parsed)]
            return sum(decoded)
        else:
            raise ValueError

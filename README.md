# Roman numeral conversion
Utility class to convert Arabic numerals (1, 2, 3) to their Roman (I, II, III) counterparts and vice versa. 

__Note:__
* Handles 0's
* Upper limit set to 3,999
* Checks invalid input

## Usage

```
from convert import Convert

Convert().toRoman(number=2421)
// returns MMCDXXI 

Convert().toArabic(number='MMCDXXI')
// returns 2421 
```

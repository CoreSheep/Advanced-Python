
"""
Regular Expression

1. Package 
import re

2. Key functions
 - findall: return a list of all matched strings
    re.findall(pattern, string, flag)
 - search: return a match obj
    re.search(pattern, string, flag)
    
 
 3. Metacharacters
  - . any character
  - * zero or one more
  - + at least one
  - ? zero or one
  - ^ start with "^hello"
  - $ end with "world$"
  - | either "apple|banana"
  - [] a group of character [a-z][A-Z]
  - '\' special sequence (e.g. 'd' digit, 's' space, 'w' word character a-z, 0-9, and '_' underscore )
  - set of characters
    1. [0-9], [a-z], [A-Z] return a match if it contains any character inside the set
    2. [^abc] return a match if it does not contain any ...
    3. [0-9][0-9] return two digits
 
"""
import re

# 1. find all letter and digits in a string
letters = re.findall("[a-zA-Z0-9]", "abc0934lijiufeng!@0924")
print(letters)
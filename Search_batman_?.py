#This function searches text for batman/batwoman w/ regular expressions

import re

message = 'The Adventures of Batman'

batRegex = re.compile(r'Bat(wo)?man') #the ? says we can have paren either 0 or 1 time.

#Can also do r'Batman|Batwoman'

mo = batRegex.search(message)
print(mo.group())

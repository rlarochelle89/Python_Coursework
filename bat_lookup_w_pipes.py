#This function searches text for bat-stuff w/ regular expressions

import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9900 for my office line.'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel so we need the Batcopter, ya batbat')
print(mo.group())

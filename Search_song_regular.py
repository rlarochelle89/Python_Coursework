#This function searches text for batman/batwoman w/ regular expressions

import re

song = '''12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8
maids a milking, 7 swans swimming, 6 geese a laying, 5 gold rings, 4 calling birds,
3 french hens, 2 turtle doves, and 1 partridge in a pear tree.'''

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(song)
print(mo)

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo2 = vowelRegex.findall('Robocop eats baby food')
print(mo2)

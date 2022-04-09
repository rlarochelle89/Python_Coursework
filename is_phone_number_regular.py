#This function identifies a phone number with regular expressions

import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9900 for my office line.'

PhoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matched_object = PhoneNumRegex.search(message)
matched_objects = PhoneNumRegex.findall(message)
print(matched_object.group())
print(matched_object.group(1))
print(matched_object.group(2))
print(matched_objects)

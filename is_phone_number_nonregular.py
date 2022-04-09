#This function identifies a phone number without regular expressions

def IsPhoneNum(text):
    if len(text) != 12:
        return False #phone numbers are 12 characters long with dashes
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False #missing area code
    if text[3] != '-':
        return False #missing first dash
    for i in range (4,7):
        if not text[i].isdecimal():
            return False #missing middle 3 numbers
    if text[7] != '-':
        return False #missing second dash
    for i in range (8,12):
        if not text[i].isdecimal():
            return False #missing last 4 numbers
    return True

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9900 for my office line.'

FoundNumber = False
for i in range(len(message)):
    chunk = message[i:i + 12]
    if IsPhoneNum(chunk) == True:
        print('Phone Number Found: ' + chunk)
        FoundNumber = True
if not FoundNumber == True:
    print('Could not find any phone numbers')

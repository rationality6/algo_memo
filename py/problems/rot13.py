def rot13(message):
    lower_s = message
    result = ""
    for i in range(len(lower_s)):
        if lower_s[i] in " ?!()*&^%$#+-1234567890.":
            result += lower_s[i]
        elif lower_s[i].isupper():
            result += (chr(65 + ((ord(lower_s[i]) - 65 - 13) % 26)))
        else:
            result += (chr(97 + ((ord(lower_s[i]) - 97 - 13) % 26)))
    return result


import string
from codecs import encode as _dont_use_this_
from string import maketrans, lowercase, uppercase
def rot13(message):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return message.translate(lower).translate(upper)


import string
def rot13(message):
    return message.encode("rot13")
    #oh snap


print(rot13("Why did the chicken cross the road?"))
print(rot13("test"))
# print(rot13("Why did the chicken cross the road? \n Gb trg gb gur bgure fvqr!"))
# "Jul qvq gur puvpxra pebff gur ebnq? \n To get to the other side!"

print(ord("A"))

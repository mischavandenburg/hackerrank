'''
A valid email address meets the following criteria:
It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is , , or  characters in length.
Given  pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.
Hint: Try using Email.utils() to complete this challenge. For example, this code:

Solution by Mischa van den Burg
www.mischavandenburg.com
'''

import email.utils, re

num = int(raw_input())
regex = re.compile(r"(^[a-z])([a-zA-Z0-9\-\_\.]+)(@)([a-z]+)(\.)([a-z]{1,3}$)")

for i in range(num):
    a = email.utils.parseaddr(raw_input())
    if regex.search(a[1]):
        print(email.utils.formataddr(a))
    
    



import string
import random

def randomString(stringLength=10):
     """Generate a random string of fixed length """
     letters = string.hexdigits
     return ''.join(random.choice(letters) for i in range(stringLength))

def getjson():
     s1, s2 = randomString(26), randomString(26)
     print('{')
     print(f' "sender" : "{s1}",')
     print(f' "recipient" : "{s2}",')
     print(f' "amount" : {random.randint(1, 101)}')
     print('}')

i = ''
while i != 'quit':
    getjson()
    i = input('Press enter to continue or "quit" to exit.')

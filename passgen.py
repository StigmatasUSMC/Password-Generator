import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = "[]{}()*;/,-_"

full = lower + upper + numbers + symbols

length = 16
password = "".join(random.sample(full,length))
print(password)

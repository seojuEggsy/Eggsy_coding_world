from random import *

byte_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

return_str = ''
for i in range(11):
    return_str += choice(byte_list)

print(return_str)
# import numpy as np
#
# testBoard = [
#     ['X', 'O', 'O', 'O', 'X'],
#     ['X', 'O', 'O', 'O', 'O'],
#     ['X', 'X', 'O', 'O', 'O'],
#     ['X', 'X', 'O', 'O', 'O'],
#     ['X', 'X', 'X', 'X', 'X']
# ]
#
# a = np.array(testBoard)
# print(a)



import hashlib
m = hashlib.sha256()
print(m)
m.update(b"Nobody instpects")
print(m)
m.update(b"the spammish repetition")
print(m)
print(m.digest())
print(m.digest_size)
print(m.block_size)

import hashlib
a = hashlib.sha256(b"aweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofjaweijfewoifjweiofjweiofjweiofjweiofj").hexdigest()
print(a)

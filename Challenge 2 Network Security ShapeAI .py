#Generate hashes of string data using 3 Algorithms from hashlib

import hashlib
str1="Ambar Mittal"

#Using sha1 Algorithm
Hashed_1=hashlib.sha1(str1.encode()).hexdigest()
print("Hashed Password using sha1:",Hashed_1)

#Using blake2b Algorithm
Hashed_2=hashlib.blake2b(str1.encode()).hexdigest()
print("Hashed Password using blake2b:",Hashed_2)

#Using sha3_224 Algorithm
Hashed_3=hashlib.sha3_224(str1.encode()).hexdigest()
print("Hashed password using sha3_224:",Hashed_3)

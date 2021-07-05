#program to generate md5 of string data

import hashlib
str1="test_password"
Hashed=hashlib.md5(str1.encode()).hexdigest()
print("Hashed Password using Md5",Hashed)

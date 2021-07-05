#Add Salting and Iterations to your hashes

import hashlib
import bcrypt
password = 'test_password'
salt=str(bcrypt.gensalt())

passwd= salt + password 

hashed_password = hashlib.md5(passwd.encode()).hexdigest()


for i in range(2,6):
    hashed_password =hashlib.md5(hashed_password.encode()).hexdigest()
print("Hashed Password after hashing it 5 Times using Md5 Algoithm::",hashed_password)

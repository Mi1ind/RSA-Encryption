# Note that hash is one way (useful for paswords.)
import hashlib

password = 'Hi my name is Milind'
hashedPass = hashlib.md5(password)

print(hashedPass)
print(hashedPass.hexdigest())

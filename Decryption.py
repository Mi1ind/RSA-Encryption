from Encryption import encrypt


class decrypt():

    def maths(self, cipherTxt):
        privateKey = [143, 103]
        num = (cipherTxt**privateKey[1]) % privateKey[0]
        print(num)

    def numToStr(self, asciiNum):
        print(chr(asciiNum))


newInstance = decrypt()
newInstance.maths(2)
newInstance.numToStr(63)

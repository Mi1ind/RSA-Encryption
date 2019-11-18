class decrypt():

    def maths(self, cipherTxt):
        privateKey = [103, 143]
        num = (cipherTxt**privateKey[0]) % privateKey[1]
        print(num)

    def numToStr(self, asciiNum):
        print(chr(asciiNum+64))


newInstance = decrypt()
newInstance.maths(110)
newInstance.numToStr(33)

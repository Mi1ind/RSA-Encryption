
class encrypt():

    def strToNum(self, txt):
        num = []
        for i in range(len(txt)):
            num.append(ord(txt[i])-64)
            # if ord(txt[i]) < 3:
            #     num.append(ord(txt[i])-64)
            # else:
            #     num.append(str('0'+str(ord(txt[i])-64)))

        print(''.join(map(str, num)))

    def maths(self, asciiTxt):
        publicKey = [7, 143]
        num = (asciiTxt**publicKey[0]) % publicKey[1]
        print(num)


newInstance = encrypt()
newInstance.strToNum('a')
newInstance.maths(33)

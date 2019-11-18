
class Encrypt(object):

    def strToNum(self, txt):
        num = []
        for i in range(len(txt)):
            num.append(ord(txt[i]))
            # if ord(txt[i]) < 3:
            #     num.append(ord(txt[i])-64)
            # else:
            #     num.append(str('0'+str(ord(txt[i])-64)))

        print(''.join(map(str, num)))

    def maths(self, asciiTxt):
        publicKey = [143, 7]
        nums = (asciiTxt**publicKey[1]) % publicKey[0]
        print(nums)


newInstance = Encrypt()
newInstance.strToNum('aa')
newInstance.maths(2)

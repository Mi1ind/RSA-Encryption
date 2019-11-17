
class encrypt():

    def strToNum(self, txt):
        num = []
        for i in range(len(txt)):
            num.append(ord(txt[i]))
        print(''.join(map(str, num)))

    def maths(self, asciiTxt):
        publicKey = [5, 14]
        num = (asciiTxt**publicKey[0]) % publicKey[1]
        print(num)


a = encrypt()
# a.strToNum('ab')
a.maths(9798)

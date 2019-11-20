
import Keys
txtInput = input()


class Encrypt(object):
    # def __init__(self, txt):
    #     self.txt = txt
        # self.asciiTxt = asciiTxt

    def strToNum(self, txt):
        num = []
        a = ''
        for i in range(len(txt)):
            num.append(ord(txt[i]))

        a = a.join(map(str, num))
        return int(a)

    def encMaths(self, asciiTxt):

        nums = (asciiTxt**Keys.publicKey[1]) % Keys.publicKey[0]
        return (nums)

    def encAnswer(self):
        Inst = Encrypt()
        cipherTxt = Inst.encMaths(Inst.strToNum(txtInput))
        return cipherTxt


newInstance = Encrypt()

print(newInstance.strToNum(txtInput))
print(newInstance.encAnswer())

import Keys
ciperTxtInput = int(input())


class Decrypt():

    def decMaths(self, cipherTxt):

        num = pow(cipherTxt, Keys.privateKey[1], Keys.privateKey[0])
        return num

    def numToStr(self, asciiNum):
        lst = [int(x) for x in str(asciiNum)]
        lst.append('*')
        answer = ''

        finalLst = []
        j = 0

        while lst[j] != '*':
            if lst[j] == 1:
                finalLst.insert(j, ''.join(map(str, lst[j:j+3])))
                j += 3
            else:
                finalLst.insert(j, ''.join(map(str, lst[j:j+2])))
                j += 2

        for i in range(len(finalLst)):
            answer += chr(int(finalLst[i]))
        return answer

    def decAnswer(self):
        Inst = Decrypt()
        scrambledTxt = Inst.decMaths(ciperTxtInput)
        string = Inst.numToStr(scrambledTxt)
        return string


newInstance = Decrypt()
# newInstance.decMaths(610)
# newInstance.numToStr(75)

print(newInstance.decAnswer())
# print(newInstance.numToStr())

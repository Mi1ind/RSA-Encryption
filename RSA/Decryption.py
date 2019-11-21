import Keys
ciperTxtInput = int(input())


class Decrypt():

    def decMaths(self, cipherTxt):
        # Instead of Brute force, explore a more computationally efficient method. Modular Exponentiation

        # set y = x
        # for bit j = k - 2 downto 0
        # begin
        # y = y * y mod n   /* square */
        # if e(j) == 1 then
        #     y = y * x mod n  /* multiply */
        # end
        # return y

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
        a = Inst.decMaths(ciperTxtInput)
        b = Inst.numToStr(a)
        return a, b


newInstance = Decrypt()
# newInstance.decMaths(610)
# newInstance.numToStr(75)

print(newInstance.decAnswer())


class encrypt():
    publicKey = [5, 14]

    def strToNum(self, txt):
        num = []
        let = 0

        # for i in range(len(txt)):
        #     num.append(my_dict[txt[i]])
        # print(num)
        for i in range(len(txt)):
            num.append(ord(txt[i]))
        print(''.join(map(str, num)))


a = encrypt()
a.strToNum('Hi I am Milind')

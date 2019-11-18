
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
        publicKey = [145906768007583323230186939349070635292401872375357164399581871019873438799005358938369571402670149802121818086292467422828157022922076746906543401224889672472407926969987100581290103199317858753663710862357656510507883714297115637342788911463535102712032765166518411726859837988672111837205085526346618740053,
                     65537]  # [N,e] where N = p*q and e is encryption key
        nums = (asciiTxt**publicKey[1]) % publicKey[0]
        print(nums)


newInstance = Encrypt()
# newInstance.strToNum("Hi my")
newInstance.maths(7210532109121)

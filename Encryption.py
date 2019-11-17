
publicKey = [5, 14]


def strToNum(txt):
    my_dict = {'A': 1, 'B': 2}
    global num
    num = []

    for i in range(len(txt)):
        num.append(my_dict[txt[i]])
    return(num)


print(num)

strToNum('AB')

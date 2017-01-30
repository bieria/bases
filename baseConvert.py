standardBase = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',\
                'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',\
                'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '`', '-',\
                '=', '[', ']', '\\', ';', "'", ',', '.', '/', '~','!', '@', '#', '$', '%', '^',\
                '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?']
def TentoX(inpNum, bits=8, targetBase=2):
    outString = []
    if inpNum >= targetBase**bits:
        raise ValueError("Input number is too large for the number of bits.\nMaximum number is %s." % str(targetBase**bits-1))
    for i in range(bits):
        currentBit = targetBase**(bits-1)
        currentValue = inpNum/currentBit
        inpNum = inpNum % currentBit
        outString.append(standardBase[currentValue])
    return ''.join(outString)

def XtoTen(inpNum, inputBase=2):
    bits = len(inpNum)
    inpBits = list(inpNum)
    outputNum = 0
    for i in range(bits):
        outputNum += standardBase.index(inpBits[i])*(inputBase**(bits-i-1))
    return outputNum

def XtoX(inpNum, startBase=2, endBase=16, bits=8):
    a = XtoTen(inpNum, startBase)
    b = TentoX(a, bits, endBase)
    return b
while True:
    print "What base do you want to convert from?"
    a = input(">>")
    print "What number do you want to convert?"
    b = raw_input(">>")
    print "What base do you want to convert to?"
    c = input(">>")
    print XtoX(b, a, c, 8)

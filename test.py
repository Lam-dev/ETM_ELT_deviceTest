def __ToHex8bit(number):
    hexStr = hex(seriElem)[2:]
    if(len(hexStr) == 1):
        return "0"+ hexStr
    else:
        return hexStr

macString = "02:81:B3:28:41:4A"
lstByteStrType = macString.split(":")
lstByteMacIntType = [int(elem, 16) for elem in lstByteStrType]
seriString = "   "
for i in range(3, 6):
    seriElem = lstByteMacIntType[i] ^ 69
    seriString += "" + __ToHex8bit(seriElem)
print(seriString)


def convertToHex(str):
    return int(str,base=16)

def XOR(str1,str2):
    a = convertToHex(str1)
    b = convertToHex(str2)
    return hex(a ^ b)

print(XOR("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965"))
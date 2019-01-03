#!/usr/bin/python
# -*- coding: UTF-8 -*-

S=[
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

S1=[
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]

Rcon=[
    0x01000000, 0x02000000,
    0x04000000, 0x08000000,
    0x10000000, 0x20000000,
    0x40000000, 0x80000000,
    0x1b000000, 0x36000000
]

colM=[
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]

decolM=[
    [0xe, 0xb, 0xd, 0x9],
    [0x9, 0xe, 0xb, 0xd],
    [0xd, 0x9, 0xe, 0xb],
    [0xb, 0xd, 0x9, 0xe]
]

def char2bin(s):
    temp = ""
    for c in s:
        temp += bin(ord(c))[2:].zfill(8)
    return temp.ljust(64, "0")

def shift(s, i):
    x = list(s[:i])
    x.reverse()
    y = list(s[i:])
    y.reverse()
    return ''.join(list(reversed(x + y)))

def xor(key, R, n):
    xor_result = ""
    for i in range(n):
        xor_result += str(int(R[i]) ^ int(key[i]))
    return xor_result

def hexxor(a,b,n):
    xor_result = ""
    for i in range(n):
        xor_result += hex(int(a[i],16) ^ int(b[i],16))[2:]
    return xor_result

def GF2mul(b):
    # 如果原始值的最高位为1，则还需要将左移一位后的结果异或00011011
    if b >= 128:
        b = (b - 128) * 2
        return b ^ 27
    else:
        return b * 2

#a=3,可以拆成先分别乘以(0000 0001)和(0000 0010)，再将两个乘积异或
def GF3mul(b):
    return GF2mul(b)^b

def GF4mul(b):
    return GF2mul(GF2mul(b))

def GF8mul(b):
    return GF2mul(GF4mul(b))

def GF9mul(b):
    return GF8mul(b)^b

def GF11mul(b):
    return GF9mul(b)^GF2mul(b)

def GF12mul(b):
    return GF8mul(b)^GF4mul(b)

def GF13mul(b):
    return GF12mul(b)^b

def GF14mul(b):
    return GF12mul(b)^GF2mul(b)

def GF(a,b):
    if a==1:
        return b
    elif a==2:
        return GF2mul(b)
    elif a==3:
        return GF3mul(b)
    elif a==9:
        return GF9mul(b)
    elif a==11:
        return GF11mul(b)
    elif a==13:
        return GF13mul(b)
    elif a==14:
        return GF14mul(b)

class AES:
    '''
    key:初始密钥
    W：44个子密钥
    matrixplainText：加密矩阵
    matrixcryptText：解密矩阵
    newplainText：解密后出来的文本·
    '''
    def __init__(self, key,plainText,hexcryptText):
        self.key = key
        self.binkey = ""
        self.hexkey=""
        self.W=[]

        self.plainText=plainText
        self.hexplainText=""
        self.matrixplainText=[]

        self.cryptText=""
        self.hexcryptText = hexcryptText
        self.matrixcryptText=[]

        self.newplainText=""


    #初始化矩阵
    def str2matrix(self):
        for i in xrange(0,4):
            one=[]
            for j in xrange(0,16,4):
                one.append(self.hexplainText[(i+j)*2:(i+j)*2+2])
            self.matrixplainText.append(one)

    #字节代替,根据Sbox决定是S盒替换还是逆S盒替换
    def subBytes(self,Sbox):
        for i in range(4):
            for j in range(4):
                row = int(self.matrixplainText[i][j][:1], 16)
                col = int(self.matrixplainText[i][j][1:], 16)
                num = row * 16 + col
                self.matrixplainText[i][j]= hex(Sbox[num])[2:].zfill(2)
    #逆字节替换
    def InvsubBytes(self,Sbox):
        for i in range(4):
            for j in range(4):
                row = int(self.matrixcryptText[i][j][:1], 16)
                col = int(self.matrixcryptText[i][j][1:], 16)
                num = row * 16 + col
                self.matrixcryptText[i][j]= hex(Sbox[num])[2:].zfill(2)

    #行位移
    def ShiftRows(self):
        for i in range(1, 4):
            b = self.matrixplainText[i][:i]
            b.reverse()
            c = self.matrixplainText[i][i:]
            c.reverse()
            self.matrixplainText[i] = list(reversed(b + c))

    #逆行位移
    def InvShiftRows(self):
        for i in range(1,4):
            b=self.matrixcryptText[i][-i:]
            b.reverse()
            c=self.matrixcryptText[i][:-i]
            c.reverse()
            self.matrixcryptText[i]=list(reversed(c+b))


    #列混淆
    def MixColumns(self):
        temp=[ [ 0 for i in range(4) ] for j in range(4) ]

        for k in range(4):
            for i in range(4):
                temp[k][i] =GF(int(colM[k][0]),int(self.matrixplainText[0][i], 16))
                for j in range(1,4):
                    temp[k][i] =temp[k][i]^GF(int(colM[k][j]),int(self.matrixplainText[j][i],16))

        for i in range(4):
            for j in range(4):
                self.matrixplainText[i][j]=hex(temp[i][j])[2:].zfill(2)

    #逆列混淆
    def InvMixColumns(self):
        temp = [[0 for i in range(4)] for j in range(4)]

        for k in range(4):
            for i in range(4):
                temp[k][i] = GF(decolM[k][0], int(self.matrixcryptText[0][i], 16))
                for j in range(1, 4):
                    temp[k][i] = temp[k][i] ^ GF(decolM[k][j], int(self.matrixcryptText[j][i], 16))

        for i in range(4):
            for j in range(4):
                self.matrixcryptText[i][j] = hex(temp[i][j])[2:].zfill(2)

    # 轮密相加
    def AddRoundKey(self,k):
        for i in range(4):
            for j in range(4):
                self.matrixplainText[j][i]=hexxor(self.W[4*k+i][j*2:j*2+2],self.matrixplainText[j][i],2)

    def InvAddRoundKey(self,k):
        for i in range(4):
            for j in range(4):
                self.matrixcryptText[j][i]=hexxor(self.W[39-4*(k+1)+i+1][j*2:j*2+2],self.matrixcryptText[j][i],2)

    def T(self,s,j):
        #字循环
        temp=shift(s,8)

        tempS=""
        #字节代换
        for i in xrange(0,8,2):
            row=int(temp[i:i+1],16)
            col=int(temp[i+1:i+2],16)
            num=row*16+col
            tempS += hex(S[num])[2:].zfill(2)
        #轮常量异或
        return hexxor(tempS,hex(Rcon[j])[2:].zfill(8),8)

    #密钥膨胀
    def generateKeys(self):
        self.binkey = char2bin(self.key[:8])
        self.binkey += char2bin(self.key[8:])

        self.hexkey=hex(int(self.binkey,2))[2:-1]

        #初始的4个密钥直接添加
        for i in xrange(0, 32, 8):
            self.W.append(self.hexkey[i:i+8])

        #添加后面的40个密钥
        for i in range(4,44):
            #如果i不是4的倍数，则W[i]=W[i-4]⨁W[i-1]
            if i%4!=0:
                self.W.append(hexxor(self.W[i-4],self.W[i-1],8))
            #如果i是4的倍数，则W[i]=W[i-4]⨁T(W[i-1])
            else:
                self.W.append(hexxor(self.W[i - 4],self.T(self.W[i - 1],i/4-1),8))

        #for i in range(44):
            #print "密钥{:0>2d}:{}".format(i+1,self.W[i])


    def encrypt(self,tempstr):

        for i in range(16):
            self.hexplainText+=hex(ord(tempstr[i:i+1]))[2:].zfill(2)

        #转成矩阵
        self.str2matrix()
        self.AddRoundKey(0)
        #九轮加密
        for i in range(9):
            #print "加密第{:0>2}轮：".format(i+1)
            self.subBytes(S)
            self.ShiftRows()
            self.MixColumns()
            self.AddRoundKey(i+1)

        #print "加密第10轮："
        self.subBytes(S)
        self.ShiftRows()
        self.AddRoundKey(10)

        '''
        print "加密十轮之后的密钥矩阵："
        for k in range(4):
            print self.matrixplainText[k]
        #转换成密文字符
        for i in range(4):
            for j in range(4):
                self.cryptText+=chr(int(self.matrixplainText[i][j],16))
        
        print "密文是：",self.cryptText
        '''
        for i in range(4):
            for j in range(4):
                self.hexcryptText += self.matrixplainText[i][j]


    #明文长度大于16位时，分组进行加密
    def allEncrypt(self):
        self.generateKeys()
        length=len(self.plainText)
        num=length/16
        remainder=length%16

        if remainder!=0:
            self.plainText+='0'*(16-remainder)
        nowLength=len(self.plainText)
        #print length,num,remainder,len(self.plainText),self.plainText

        count=0
        for i in xrange(0,nowLength,16):
            count+=1
            self.encrypt(self.plainText[i:i+16])
            self.matrixplainText=[]
            self.hexplainText=""
        #print "AES密文：",count,len(self.hexcryptText), self.hexcryptText
        return len(self.hexcryptText), self.hexcryptText

    def allDecrypt(self):
        self.generateKeys()
        length=len(self.hexcryptText)
        num=length/32


        for i in xrange(0,length,32):
            temp=self.hexcryptText[i:i+32]

            for j in xrange(0,32,8):
                tempOne = []
                for k in xrange(0,8,2):
                    tempOne.append(temp[j+k:j+k+2])
                self.matrixcryptText.append(tempOne)
            self.decrypt()
            self.matrixcryptText = []
        return len(self.newplainText),self.newplainText



    def decrypt(self):
        #self.matrixcryptText=self.matrixplainText

        self.InvAddRoundKey(-1)

        for i in range(9):
            #print "解密第{:0>2}轮：".format(i + 1)
            self.InvShiftRows()
            self.InvsubBytes(S1)
            self.InvAddRoundKey(i)
            self.InvMixColumns()
            #for k in range(4):
                #print self.matrixcryptText[k]

        #print "解密第10轮："
        self.InvShiftRows()
        self.InvsubBytes(S1)
        self.InvAddRoundKey(9)
        #for k in range(4):
            #print self.matrixcryptText[k]

        for i in range(4):
            for j in range(4):
                self.newplainText+=chr(int(self.matrixcryptText[j][i],16))
        #print "密文解密后是：",self.newplainText

def enter():
    key = "abcdefgh12345678"
    #plainText = "tomorrowcrackyou"
    plainText="Do not go gentle into that good night883392545e49c12b33ba2c5ec16a3e49343349c1492c88ba34338888882cd907"

    #key=raw_input("输入16位密钥：")
    #plainText=raw_input("输入16位明文：")

    test = AES(key,plainText)
    test.allEncrypt()
    test.allDecrypt()
    #test.decrypt()

if __name__ == '__main__':
    enter()

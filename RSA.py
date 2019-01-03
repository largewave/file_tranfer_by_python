#!/usr/bin/python
# -*- coding: UTF-8 -*-

def getgcd(a,b):
	if b==0:
		return 1,0
	else:
		k=a//b
		remainder=a%b
		x1,y1=getgcd(b,remainder)
		x,y=y1,x1-k*y1
	return x,y

def Coprime(a,b):
    tempA=a
    temp=0
    while b!=0:
        temp=b
        b=a%b
        a=temp

    if a==1:
        print tempA,


class RSA:
    def __init__(self,plainText,hexcryptText,p,q,e,n):
        self.plainText=plainText
        self.hexcryptText=hexcryptText
        self.cryptText=[]
        self.decryptText=[]

        self.p=p
        self.q=q

        self.n=n
        self.r=0
        self.e=e
        self.d=0

    def calcN(self):
        self.n=self.q*self.p

    def calcR(self):
        self.r=(self.p-1)*(self.q-1)

    #选择e并且生成私钥d
    def choose(self):
        if self.e==0:
            print "从下面的与r互质的数中选择一个，作为e"
            for i in range(self.r):
                #判断是否是和r互质的数
                Coprime(i,self.r)
            self.e=int(raw_input("\n输入你所选的e："))
        #计算d的值
        x,y=getgcd(self.r,self.e)
        if y<0:
            self.d=y+self.r
        else:
            self.d=y

    #生成一系列公钥私钥
    def generateKeys(self):
        self.calcN()
        self.calcR()
        self.choose()

        #print "公钥(e,n):({0},{1}) 私钥(d,n):({2},{1})".format(self.e,self.n,self.d)
        return self.e,self.n

    def encrypt(self):
        self.generateKeys()
        for i in self.plainText:
            self.cryptText.append(((ord(i) ) ** self.e) % self.n)
            '''
            if i.isdigit():
                self.cryptText.append(((ord(i) - 47) ** self.e) % self.n)
            elif i.isalpha():
                self.cryptText.append(((ord(i)-96)**self.e)%self.n)
                '''
        '''
        print "RSA密文是："
        for i in self.cryptText:
            print i,
        '''
        temp=""
        for i in self.cryptText:
            temp+=hex(i)[2:-1].zfill(2)

        return len(temp),temp



    def decrypt(self):
        self.choose()
        print self.d
        print self.n
        length=len(self.hexcryptText)
        for i in xrange(0,length,2):
            self.decryptText.append(chr((int(self.hexcryptText[i:i+2],16) ** self.d) % self.n))
        print self.decryptText
        '''
        for i in self.cryptText:
            #self.decryptText.append(chr((i**self.d)%self.n+96))
            self.decryptText.append(chr((i ** self.d) % self.n ))

        print "\n解密后的明文是："
        for i in self.decryptText:
            print i,
        '''
    def SKencrypt(self):
        self.generateKeys()
        for i in self.plainText:
            self.cryptText.append(((ord(i) ) ** self.d) % self.n)
            '''
            if i.isdigit():
                self.cryptText.append(((ord(i) - 47) ** self.e) % self.n)
            elif i.isalpha():
                self.cryptText.append(((ord(i)-96)**self.e)%self.n)
                '''
        '''
        print "RSA密文是："
        for i in self.cryptText:
            print i,
        '''
        temp=""
        for i in self.cryptText:
            temp+=hex(i)[2:-1].zfill(2)

        return len(temp),temp

    def PKdecrypt(self):
        length=len(self.hexcryptText)
        for i in xrange(0,length,2):
            self.decryptText.append(chr((int(self.hexcryptText[i:i+2],16) ** self.e) % self.n))
        return ''.join(self.decryptText)

    def PKencrypt(self):
        #self.generateKeys()
        for i in self.plainText:
            self.cryptText.append(((ord(i) ) ** self.e) % self.n)
            '''
            if i.isdigit():
                self.cryptText.append(((ord(i) - 47) ** self.e) % self.n)
            elif i.isalpha():
                self.cryptText.append(((ord(i)-96)**self.e)%self.n)
                '''
        '''
        print "RSA密文是："
        for i in self.cryptText:
            print i,
        '''
        temp=""
        for i in self.cryptText:
            temp+=hex(i)[2:-1].zfill(3)

        return temp

    def SKdecrypt(self):
        self.generateKeys()
        length=len(self.hexcryptText)
        for i in xrange(0,length,3):
            self.decryptText.append(chr((int(self.hexcryptText[i:i+3],16) ** self.d) % self.n))
        return ''.join(self.decryptText)


def enter():
    #plainText=raw_input("输入明文：").lower()
    #p=int(raw_input("输入密钥p："))
    #q=int(raw_input("输入密钥q："))
    plainText="f302d9a13ecdab89439a9cfe43fffc76"
    p=13
    q=17

    test=RSA(plainText,p,q)
    #test.generateKeys()
    test.encrypt()
    test.decrypt()


if __name__ == '__main__':
    enter()
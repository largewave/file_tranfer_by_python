#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import MD5
import RSA
import AES
import hashlib

import re
import socket
import threading
import os
import random
import string
import time
import wx


bind_ip = "0.0.0.0"
bind_port = 9999

p=13
q=17


info = dict()
jiedan = ""


def fileTranfer(filename,BRSApublickeye,BRSApublickeyn):
    pattern=r"\.[^.\\/:*?\"<>|\r\n]+$"

    #step0:打开文件，读取文件内容作为明文
    #print "#"*100
    #filename=raw_input("输入你的文件名：")
    result=re.findall(pattern,filename)
    if result[0]==".txt":
        with open("D:\\python\\code\\"+filename, 'r') as f:
            plainText = ''.join(f.readlines())
    elif result[0]==".jpg":
        with open("D:\\python\\code\\"+filename, 'rb') as f:
            plainText = ''.join(f.readlines())
    else:
        with open("D:\\python\\code\\"+filename, 'rb') as f:
            plainText = ''.join(f.read())
    print "打开文件成功=>",


    #step1:对明文使用MD5算法进行哈希
    #print "#" * 100
    #myMD5=MD5.MD5(plainText)
    #myhash=myMD5.encrypt()
    #print "哈希值是：",myhash
    myMD5=hashlib.md5()
    myMD5.update(plainText)
    myhash=myMD5.hexdigest()
    print "生成哈希值成功=>",


    #step2：对哈希值使用RSA进行数字签名
    #print "#" * 100
    #print "RSA算法进行数字签名："
    #p=int(raw_input("输入私钥p:"))
    #q=int(raw_input("输入私钥q:"))
    myRSA=RSA.RSA(myhash,"",p,q,107,0)
    myRSAlength,myDigitalSignature=myRSA.SKencrypt()
    print "生成数字签名成功=>",


    #step3：将明文和数字签名的值连接起来，使用AES算法进行对称加密
    #print "#" * 100
    MplusE=plainText+myDigitalSignature
    #print "明文和经过数字签名的哈希值连接：\n长度为：",len(MplusE),MplusE


    #step4:使用AES对称加密算法对明文和哈希值进行加密
    #print "#" * 100
    #AESkey=raw_input("输入AES密钥：")
    AESkey= ''.join(random.sample(string.ascii_letters + string.digits, 16)).lower()
    print "生成随机AESKEY:%s=>"%AESkey,
    BRSA=RSA.RSA(AESkey,"",0,0,BRSApublickeye,BRSApublickeyn)
    SecretAESkey=BRSA.PKencrypt()

    myAES=AES.AES(AESkey,MplusE,"")
    myAESlength,mySecretText=myAES.allEncrypt()

    finalSecretText=SecretAESkey+mySecretText
    print "生成最终密文=>"


    return finalSecretText




def handle_client(client_socket):
    #接受B的公钥
    BRSApublickeye = int(client_socket.recv(1024))
    BRSApublickeyn = int(client_socket.recv(1024))


    #生成A的公钥
    myRSA = RSA.RSA("", "", p, q, 107, 0)
    ARSApublickeye, ARSApublickeyn = myRSA.generateKeys()
    client_socket.send(str(ARSApublickeye))
    time.sleep(1)
    client_socket.send(str(ARSApublickeyn))
    time.sleep(1)

    path="D:/python/code"
    files=os.listdir(path)
    client_socket.send("\n".join(files))

    while True:
        request = client_socket.recv(1024)

        if request.find('#') == -1:
            print "对方请求传输%s"%request
            finalSecretText=fileTranfer(request,BRSApublickeye,BRSApublickeyn)
            client_socket.send(str(len(finalSecretText)))
            time.sleep(3)
            client_socket.send(finalSecretText)
            '''
            num=len(finalSecretText)/1024
            for i in range(num):
                print "第%d次传输"%i
                client_socket.send(finalSecretText[i*1024:(i+1)*1024])
                time.sleep(2)
            '''
            print "传输成功!"
        #jiedan = request.split('#')[0]
        #print request.split('#')[0]
        #print request.split('#')[1]
        #info[request.split('#')[1]].send(jiedan)
        else:
            client_socket.close()

    #print "[*] Received: %s" % request

    #client_socket.close()



def server_start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((bind_ip, bind_port))

    SEND_BUF_SIZE=1024
    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_BUF_SIZE)

    server.listen(5)

    while True:
        client, addr = server.accept()

        print "[*] Accepted connection from %s:%d" % (addr[0], addr[1])

        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == '__main__':
    server_start()


'''
    BRSApublickeye=107
    BRSApublickeyn=437
    ARSApublickeye=107
    ARSApublickeyn=221
    request="filetranfer.txt"
    finalSecretText = fileTranfer(request, BRSApublickeye, BRSApublickeyn)
    
    '''





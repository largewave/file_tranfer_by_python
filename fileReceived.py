#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import MD5
import RSA
import AES

import re
import socket
import hashlib

p = 19
q = 23


def fileTranfer(secretText, RSApublickeye, RSApublickeyn):
    # step1:使用AES算法解密
    # print "#" * 100
    # secretText=raw_input("输入需要解密的密文：")
    SecretAESkey = secretText[0:48]
    BRSA = RSA.RSA("", SecretAESkey, p, q, 107, 0)
    AESkey = BRSA.SKdecrypt()
    print "解密得到AESkey：%s=>"%AESkey,
    # AESkey = raw_input("输入AES密钥")
    myAES = AES.AES(AESkey, "", secretText[48:])
    Mlength, M = myAES.allDecrypt()

    # step2: 去掉填充0，分离明文和数字签名值
    for i in xrange(-1, -17, -1):
        if M[i] != '0':
            break
    M = M[:i + 1]

    myplainText = M[:len(M) - 64]
    myDigitalSignature = M[-64::]
    print "分离明文和数字签名成功=>",

    # step3：利用RSA算法分析出哈希值
    # print "#" * 100
    # RSApublickeye=int(raw_input("输入RSA解密的公钥e:"))
    # RSApublickeyn=int(raw_input("输入RSA解密的公钥n:"))
    myRSA = RSA.RSA("", myDigitalSignature, 0, 0, RSApublickeye, RSApublickeyn)
    myhash = myRSA.PKdecrypt()
    print "RSA解密出hash值=>",

    # step4:对明文使用MD5算法进行哈希
    # print "#" * 100
    # myMD5 = MD5.MD5(myplainText)
    # calhash = myMD5.encrypt()
    myMD5 = hashlib.md5()
    myMD5.update(myplainText)  # .encode(encoding='utf-8'))
    calhash = myMD5.hexdigest()
    print "计算哈希值成功=>",

    # step5:比较哈希是否相同，相同将明文内容写入文件中
    if calhash == myhash:
        print "hash相同，传输内容未被篡改"
        pattern = r"\.[^.\\/:*?\"<>|\r\n]+$"
        filename = raw_input("输入你要保存的文件名：")
        result = re.findall(pattern, filename)
        if result[0] == ".txt":
            with open("/root/code/panice/xbz/" + filename, 'w') as f:
                f.write(myplainText)
        elif result[0] == ".jpg":
            with open("/root/code/panice/xbz/" + filename, 'wb') as f:
                f.write(myplainText)
        with open("/root/code/panice/xbz/temp.txt", 'w') as f:
            f.write(secretText)
        print "将解密出来的明文和密文分别写进%s和temp.txt文件中，请查看！" % filename
    else:
        print "hash不同，文本错误！"


def clientStart():
    host = raw_input("输入服务端ip：")
    port = int(raw_input("输入服务端端口："))
    addr = (host, port)
    RECV_BUF_SIZE = 1024

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)

    client.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_BUF_SIZE
    )

    myRSA = RSA.RSA("", "", p, q, 107, 0)
    BRSApublickeye, BRSApublickeyn = myRSA.generateKeys()
    client.send(str(BRSApublickeye))
    client.send(str(BRSApublickeyn))

    # 接受A的公钥
    ARSApublickeye = int(client.recv(1024))
    ARSApublickeyn = int(client.recv(1024))

    print "密钥协商完成"

    secretText = ""
    while True:
        data = client.recv(1024)
        print "*"*100
        print "服务端文件列表："
        print data
        print "*" * 100
        filename = raw_input("输入想要获取的文件:")
        client.send(filename)
        res_size = client.recv(1024)
        recevied_size = 0
        print "接受加密数据进度：",
        while recevied_size < int(res_size.decode()):
            tmp_recv=client.recv(1024)
            recevied_size += len(tmp_recv)
            print "%.2f%%==>" % (recevied_size / float(res_size.decode()) * 100),
            secretText+=tmp_recv


        fileTranfer(secretText, ARSApublickeye, ARSApublickeyn)


if __name__ == '__main__':
    clientStart()

    '''
    BRSApublickeye = 107
    BRSApublickeyn = 437
    ARSApublickeye = 107
    ARSApublickeyn = 221
    secretText="0df1ab19506012d0790390c606112407e0570dd14b02d0722f5e38af2d9535ed31f085bc56541278cc1d8389916774d57088f3779f78086fd32d581ca71d83852822c15ff17a729a0f9aa60a9a16409a8fb68e0eecd09f1204e22d88fb5f266f5269480161fc5beb581ed2c818a23506669e93fe26172b256f540ebd8645935dd11a87ced2b1238e7a289979dcd956e2103d5f3d3e280952e71951aeb712eaad5a9adcffe888be8175e00c60aa0b58b775a761e826f03ff93db8304507fc4214b9913479524e4b6333539bd2d5fd7c5030799e2f1ca57682de4fa8d704c2f3b25a781b678543a9ed0aa0f796348e318605a28aa9e2880bc74a0ba4cc000c9aa6abe720fcfc1a2869ab35a43d12808a122869084c27c7edc6413eba782962fa7fa2c030790c5954e7ea24bc11f145f3f5ec583dc4fafc25ed1d8308f6211264438fd77f790f200800dd6e58d2daaae3435bcb49d7830b1ae8755150b95c137cc2d56d32716d31e7772b9db76b299d171cdc823112aaa43df83756d9a56fd4c3c0020b017f3ff2a99ce5be8788b1e4a9349bd615c7e5a5db2ed98551740f00ada998d80c1c37012c986f540ebd8645935dd11a87ced2b1238e7a289979dcd956e2103d5f3d3e280952bfc32a3f76f69e9f014133ac848534868cfcb0375609852aae1802265997742a3c93a9ab49b610532c801b05db1b1aa3e7b928ca730436e64fc74c1eac90ac07f5d1ab81b5ee1e08e84813979c002581d538fcfa203bcf32f05b23af40cc06aecde16a959342f503b4c708348be821bffd8cd217ce03f32c2f97873b18ca01d748daa38dbb71f3b519c5fcee159e8435c7f062d7bc16339fefd961c94c37a8b8ccd19783cafd59898c1e2e862b820fb74c2b8869146bd9fec7053a8b801b837dca83f1335ba7441fdb3601939eb1b66583f72cbfbf50bf79e55c6d9e871f5553eaae9697be3968fcf8243dd817d46bf2f1f573086a1c29851708787fb2dcb4dc37b2c10c233ca733d2cb6effa7c8d65d6f540ebd8645935dd11a87ced2b1238e7a289979dcd956e2103d5f3d3e280952fbed1f8ac357875745237abdaed9e7c81fdc6b898cd478c938fc360d9241af527fc3b3a37620540a48dc235410a0080e1bee8b40004ab0b349737ed0ce1753fb3c816401e95ec7b1be3e43719bea38f3683528014dd62f4d01410b13466d39cf1ca8784b6f095f8835ae747e1e2d6f9263e18cabea4ccb993896c8fb6c8ed17248daa38dbb71f3b519c5fcee159e8435a77885e958f914b65545cbc7ba4ed2d2a43d518b4f38f7f8c2412ccdf073b1877c10f102c1155089ee6c0b13262d829fcc4f5e03fa488c04aa968706ff693a3ed77d6452782517e53c3b85188bc7bd081c9ae08a21dc2a5d373ef49b93470edc81337c85be6e3d8f765f87e007c4f63bc374fb518869412e81b9eff8bbb10e45"

    fileTranfer(secretText, ARSApublickeye, ARSApublickeyn,"aa.txt")
    '''

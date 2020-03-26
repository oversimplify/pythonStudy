import requests
import time
import base64
from Crypto.Cipher import AES
headers1 = {
'Host': 'file.taodocs.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
'Accept': '*/*',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Referer': 'https://www.taodocs.com/p-107648150.html',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
}
headers2={'Host': 'www.taodocs.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
'Accept': '*/*',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Referer':'https://www.taodocs.com/p-107648150.html',
'Cache-Control': 'max-age=0',
'TE': 'Trailers',}
def getimgs(url):
    pid = url.split('-')[1][:-5]#截取pid
    print(pid)
    response=requests.get('https://www.taodocs.com/showProduct.aspx?fn=docinfo&id=' + pid, headers=headers2)
    nextstr = response.json()['nextPageStr']#获取第一个nextstr
    title = response.json()['data'][0]['Title']#获取文档标题
    print(title)
    imglist=[]
    i=1
    while(nextstr):#循环获取nextstr，直到nextstr为空
        url2='https://file.taodocs.com:808/?from=pc_'+pid+'&furl='+nextstr#构造请求        
        response1 = requests.get(url2, headers=headers1).json()        
        try:
            imglist=response1['imgs']#获取imgs            
        except:
            print("=================================wait===================================")
            time.sleep(30)#遇错后延迟，主要是服务器有时间间隔限制
            response1 = requests.get(url2, headers=headers1).json()
            imglist=response1['imgs']       
        for img in imglist:
            imgjiemi=aes_decode(img, '1234567812345678')#解密，这里我把秘钥隐去了
            url = 'https:' + imgjiemi
            print(url)
            response = requests.get(url)
            imgbody = response.content
            with open('d:/develop/pyhoneStudy/file/' + title+str(i+imglist.index(img) )+ '.jpg', 'wb') as f:
                f.write(imgbody)#下载保存，没有合成pdf，主要是累了
        i=i+len(imglist)
        nextstr=response1['next']        
         
def aes_decode(data, key):#解密函数
    try:
        aes = AES.new(str.encode(key), AES.MODE_ECB)  # 初始化加密器
        decrypted_text = aes.decrypt(base64.decodebytes(bytes(data, encoding='utf8'))).decode("utf8")  # 解密
        decrypted_text = decrypted_text[:-ord(decrypted_text[-1])]  # 去除多余补位
    except Exception as e:
        print(e)
    return decrypted_text
urltoStart='https://www.taodocs.com/p-228424670.html'
getimgs(urltoStart)
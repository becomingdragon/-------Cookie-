# 使用的场景：数据采集的时候，需要绕过登陆 然后进入到某个页面
import urllib.request
import urllib.error

url = 'https://weibo.cn/7679740078/info'
headers={
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
'Cookie':
'SUB=_2A25IhBlpDeRhGeFI7FsW9C7MzDSIHXVr-BShrDV6PUJbkdAGLWjRkW1NfMhPg3rV5H9Pljf7dWOV1I6OMSNqW8Dk; SCF=ArejQ87Qhxnr71Qwcn0o_8X3e2r8HRYLUCXM1-v7Cvj2dwcM9qzj0Jmdvzjmoj1Qy97pSBvMQv8nAc15JZOW2Lk.; SSOLoginState=1702914361',
# 判断这个路径是不是由上一个路径来的 一般情况是做图片的防盗链
'Referer':'https://weibo.cn/',

 }

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)
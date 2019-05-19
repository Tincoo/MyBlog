import re
import pymysql
import csv
import time
import requests
import multiprocessing
import random
import codecs
from bs4 import BeautifulSoup

count=0
#这个实际不用写这么多，为了防止被封，就多写点吧
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",#user_agent_list[random.randint(0, 5)],
    'Connection': 'keep-alive',
    'Cookie': '这里粘贴自己cookie',
    'Host': 'www.ireadweek.com',
    'Referer': 'http://www.ireadweek.com/index.php/Index/index.html',
    'Upgrade-Insecure-Requests': '1'
}

for i in range(1,100):
    url='http://category.dangdang.com/pg'+str(i)+'-cp01.54.26.00.00.00-c143.html'
    wbdata = requests.get(url).text
    soup = BeautifulSoup(wbdata, 'html.parser')

    links = soup.select('#component_59 > li > a')
   
    print(links)


    for a in links:
        try:
            count+=1
            if(count>5000):
                break
         
            #time.sleep(random.randint(1,3))
            page_url = a.get('href')
            
            print("page_url:"+page_url)
            book_name = a.get('title')
            print(book_name)
            #存网页
            num = str(count)
            print(num)
            f=open("bookName.txt",'a')#a模式不会覆盖之前的内容
        
            f.writelines(num+':'+book_name+'\n')#r.content返回二进制形式
            f.close()
        
        except:
            print("link not found!!!")
            pass

 
'''
 wbdata2 = requests.get(page_url).content.decode('gb18030')  
        # print(wbdata2)
        soup2 = BeautifulSoup(wbdata2, 'html.parser')
        
        # product_info > div.name_info > h1
        book_name = soup2.select('#product_info > div.name_info > h1')[0].text
        print(book_name)
'''

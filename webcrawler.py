from tkinter.ttk import Style
import urllib.request as req
import bs4

manga = {"頑皮辣妹安城": "https://manga1001.com/%e3%82%84%e3%82%93%e3%81%a1%e3%82%83%e3%82%ae%e3%83%a3%e3%83%ab%e3%81%ae%e5%ae%89%e5%9f%8e%e3%81%95%e3%82%93-raw-free/",
         "徹夜之歌": "https://manga1001.com/%e3%82%88%e3%81%b5%e3%81%8b%e3%81%97%e3%81%ae%e3%81%86%e3%81%9f-%e6%bc%ab%e7%94%bb-raw-free/",
         "入間同學入魔了": "https://manga1001.com/%e9%ad%94%e5%85%a5%e3%82%8a%e3%81%be%e3%81%97%e3%81%9f%ef%bc%81%e5%85%a5%e9%96%93%e3%81%8f%e3%82%93-raw-free/",
         "血之轍": "https://manga1001.com/%e8%a1%80%e3%81%ae%e8%bd%8d-raw-free/",
         "久保同學不放過我": "https://manga1001.com/%e4%b9%85%e4%bf%9d%e3%81%95%e3%82%93%e3%81%af%e5%83%95%e3%82%92%e8%a8%b1%e3%81%95%e3%81%aa%e3%81%84-raw-free/"} 

f = open("D:\python_practices\mangalist.txt", mode="r", encoding="utf-8")

for urls in manga.values():
    request = req.Request(urls, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")                      #用beautifulsoup取得網頁html架構
    titles = root.find("table", class_="table table-hover")            #找class名為table table-hover的table標籤
    newmanga = titles.select("a", limit=1)                             #從上一行取得的table標籤往下找第一個a標籤
    new_manganame = newmanga[0].string                                 #用.string取得標籤中的文字
    new_mangaurl = newmanga[0].get("href")                             #用get取的href標籤內容
    new_num = ''.join([x for x in new_manganame if x.isdigit()])       #挑出new_manganame中的數字
    mangainfile = f.readline() 
    read_num = mangainfile.split()[1]                                  #挑出檔案中已讀過的漫畫話數
    if(new_num != read_num): 
        print(new_manganame + '\n' + new_mangaurl + '\n')

f.close()

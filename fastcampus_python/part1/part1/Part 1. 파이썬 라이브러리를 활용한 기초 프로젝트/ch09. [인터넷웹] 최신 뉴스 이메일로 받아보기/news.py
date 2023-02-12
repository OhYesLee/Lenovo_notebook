import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

# main
if __name__ == "__main__":
    inputURL = "https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y"
    response = requests.get(inputURL, headers=headers)
    beautifulSoup = BeautifulSoup(response.content, "html.parser")
    print(beautifulSoup.title.string)
    print(beautifulSoup.find("dl", attrs={"class":"type04"}).get_text())
    print(beautifulSoup.find("ul", attrs={"class":"type02"}).get_text())
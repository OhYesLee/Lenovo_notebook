import base64
from gensim.summarization.summarizer import summarize
from gensim.summarization.textcleaner import split_sentences
import collections
import textwrap
import re
import webbrowser
import os


if __name__ == "__main__":
    # 기사 이미지
    f = open("news/image", 'rb')
    image = f.readlines()
    f.close()

    # 기사 본문
    f = open("news/article", 'rb')
    article = f.readlines()
    f.close()

    # 기사 이미지 디코딩
    path = "news/image.jpg"
    file_base64 = image[0]

    with open(path, 'wb') as f:
        decoded_data = base64.decodebytes(file_base64)
        f.write(decoded_data)

    # 기사 본문 디코딩
    file_base64 = article[0]
    decoded_data = base64.decodebytes(file_base64)
    article = decoded_data.decode('utf-8')

    # 요약 텍스트 저장
    article_summarized = summarize(article, ratio=0.1)

    # 줄바꿈 정렬
    article_align = textwrap.fill(article, width=50)

    # 단어 추출
    words = re.findall(r'\w+', article_align)

    # 빈도수 산출
    counter = collections.Counter(words)

    # 키워드 추출
    keywords = counter.most_common(5)[1:]
    keys = ['# ' + elem[0] for elem in keywords]
    keys = ' '.join(keys)

    # html 파일 저장
    htmlfile = open("news/summary.html", "w")
    htmlfile.write("<html>\n")
    htmlfile.write("<h1>" + '카운트다운 들어간 아르테미스 계획…"달의 여신"은 미소지을까' + "</h2>\n")
    htmlfile.write("<img src='image.jpg'/>\n")
    htmlfile.write("<h2>" + article_summarized + "</h2>\n")
    htmlfile.write("<h2 style='background-color:powderblue;''>" + keys + "</h2>\n")
    htmlfile.write("</html>\n")
    htmlfile.close()

    webbrowser.open('file://' + os.getcwd() + "/news/summary.html")
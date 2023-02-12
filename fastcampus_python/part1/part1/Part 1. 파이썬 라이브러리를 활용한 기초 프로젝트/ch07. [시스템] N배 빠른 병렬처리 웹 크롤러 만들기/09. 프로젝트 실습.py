import logging
import platform, psutil
import os
from bs4 import BeautifulSoup
import requests

# 로거 생성
logger = logging.getLogger()

# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

# log 형식 지정
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# log 파일 생성
file_handler = logging.FileHandler('output.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def printSystemInfor():
    logger.info(f''' 
        OS                   :\t {platform.system()}
        OS Version           :\t {platform.version()}
        OS                   :\t {platform.system()}
        OS Version           :\t {platform.version()}
        Process information  :\t {platform.processor()}
        Process Architecture :\t {platform.machine()}
        CPU Cores            :\t {os.cpu_count()}   
        RAM Size             :\t {str(round(psutil.virtual_memory().total / (1024.0 **3)))+"(GB)"} 
    ''')

# 네이버 연합뉴스 URL
url1 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=100'
url2 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=101'
url3 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=102'
url4 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=103'
url5 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=104'
url6 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=105'


def web_crawler(url):
    # 헤더 설정
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

    # 서버 응답 확인
    response = requests.get(url, headers=headers)

    # BeautifulSoup 객체 생성
    beautifulSoup = BeautifulSoup(response.content, "html.parser")

    # 페이지 제목 크롤링
    print(beautifulSoup.title.string)

    # 기사 제목 크롤링
    print(beautifulSoup.find("ul", attrs={"class": "type06_headline"}).get_text())


def main(cpu=3):
    from multiprocessing import Pool
    import time

    url_list = [url1, url2, url3, url4, url5, url6]

    logger.info(f''' 멀티프로세스가 시작됩니다. ''')
    start_time = time.time()

    pool = Pool(processes=cpu)  # N개 CPU 코어를 사용합니다.
    result = pool.map(web_crawler, url_list)  # 각 URL 에 웹 크롤러 할당

    pool.close()  # 풀링 종료
    pool.join()  # 결과 합치기

    logger.info(f''' 멀티프로세스가 종료되었습니다. ''')
    logger.info("--- %s seconds ---" % (time.time() - start_time))


# Pycharm 에서 실행 확인
if __name__ == '__main__':
    import argparse
    import schedule

    ''' 입력 매개변수 설정 '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--cpu', type=int, default=3, help="멀티프로세스 CPU 수")
    parser.add_argument('--run_interval', type=int, default=5, help="웹 크롤러 실행 주기(초)")
    args = parser.parse_args()  # 매개변수 파싱
    cpu = args.cpu
    interval = args.run_interval

    logger.info(f''' 
        CPU 사용                :\t {cpu} 코어
        프로그램 실행주기        :\t {interval} 초
    ''')

    # N초에 한번씩 메인 함수 실행
    schedule.every(interval).seconds.do(main, cpu)  # 이벤트 등록

    # 스케줄러 실행
    while True:
        schedule.run_pending()


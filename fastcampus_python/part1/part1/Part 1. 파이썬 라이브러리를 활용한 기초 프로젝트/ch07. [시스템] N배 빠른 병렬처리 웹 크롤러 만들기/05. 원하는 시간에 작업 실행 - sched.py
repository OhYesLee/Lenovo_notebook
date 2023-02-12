# step1.관련 패키지 및 모듈 import
import schedule
import time


# step2.실행할 함수 선언
def message(interval):
    print(f"{interval}간격 스케줄 실행중...")


# step3.실행 주기 설정
schedule.every(1).seconds.do(message, '1초')

# step4.스캐쥴 시작
while True:
    schedule.run_pending()
    time.sleep(1)
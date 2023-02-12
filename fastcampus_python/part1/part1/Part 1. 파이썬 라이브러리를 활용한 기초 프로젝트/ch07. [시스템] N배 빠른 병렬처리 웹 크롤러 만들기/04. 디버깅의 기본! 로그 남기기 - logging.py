import logging

def myfunc():
    logger.debug("DEBUG 로그입니다.")
    logger.info("INFO 로그입니다.")
    logger.warning("WARNING 로그입니다.")
    logger.error("ERROR 로그입니다.")
    logger.critical("CRITICAL 로그입니다.")

if __name__ == "__main__":
    # 로그 생성
    logger = logging.getLogger()

    # 로그의 출력 기준 설정
    logger.setLevel(logging.DEBUG)

    # log 형식 지정
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # log 출력
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # log 파일 생성
    file_handler = logging.FileHandler('sample2.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # 함수 실행
    myfunc()
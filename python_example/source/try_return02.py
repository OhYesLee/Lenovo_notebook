# 함수를 선언합니다.
def write_text_file(filename, text):
    # try except 구문을 사용합니다.
    try:
        # 파일을 엽니다.
        file = open(filename, "w")
        # 여러 가지 처리를 수행합니다.
        return
        # 파일에 텍스트를 입력합니다.
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        # 파일을 닫습니다.
        file.close()

# 함수를 호출합니다.
write_text_file("test.txt", "안녕하세요!")
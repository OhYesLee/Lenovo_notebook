# 모듈을 읽어 들입니다.
import os

# 폴더를 읽어 들이는 함수
def read_folder(path):
    # 폴더의 요소 읽어 들이기
    output = os.listdir(path)
    # 폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(item):
            # 폴더라면 계속 읽어 들이기
            read_folder(item)
    else:
        # 파일이라면 출력하기
        print("파일:", item)
        
# 현재 폴더의 파일/폴더를 출력합니다.
read_folder(".")
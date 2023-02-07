# 모듈을 읽어 들입니다.
from urllib import request

# urlopen() 함수로 구글의 메인 페이지를 읽습니다.
target = request.urlopen("https://google.com")
output = target.read()

# 출력합니다.
print(output)
# 파일을 엽니다.
with open("basic.txt", "r") as file:
    # 파일을 읽고 출력합니다.
    contents = file.read()
print(contents)
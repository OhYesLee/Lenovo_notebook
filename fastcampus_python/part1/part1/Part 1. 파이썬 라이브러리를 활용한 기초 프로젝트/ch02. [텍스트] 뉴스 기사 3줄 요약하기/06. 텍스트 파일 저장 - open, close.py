
if __name__ == "__main__":
    # 텍스트 파일 쓰기
    f = open("새파일.txt", 'w')
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()

    # 모든 줄 읽기
    f = open("새파일.txt", 'r')
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
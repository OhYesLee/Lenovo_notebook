import base64_exp
path = "img/0005303739_001_20220828154501895.jpg"

# 바이너리 파일 읽기
with open(path, 'rb') as img:
    image = img.read()

# base64 인코딩
with open(path, 'rb') as img:
    data = img.read()
    encoded = base64.b64encode(data)

# base64 디코딩
decoded = base64.decodebytes(encoded)


# 이미지 파일로 저장
file = "img/decoded.jpg"

with open(file, 'wb') as file:
    file.write(decoded)
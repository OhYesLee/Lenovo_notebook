nucleos = input("염기 서열을 입력해주세요: ")
counter = {
    "a": 0,
    "t": 0,
    "g": 0,
    "c": 0
}

for nucleo in nucleos:
    counter[nucleo] += 1
for key in counter:
    print(f"{key}의 개수: {counter[key]}")
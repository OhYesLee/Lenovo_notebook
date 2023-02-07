from collections import Counter

nucleos = input("염기 서열을 입력해주세요: ")
counter = Counter(nucleos)

for key in counter:
    print(f"{key}의 개수: {counter[key]}")
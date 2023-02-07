nucleos = input("염기 서열을 입력해주세요: ")
counter = {}

for i in range(0, len(nucleos), 3):
    # 3글자씩 추출합니다.
    codon = nucleos[i:i+3]
    # 3글자로 구성되는지 확인합니다.
    if len(codon) == 3:
        # 딕셔너리에 키가 없을 경우 추가합니다.
        if codon not in counter:
            counter[codon] = 0
        # 갯수를 추가합니다.
        counter[codon] += 1

print(counter)
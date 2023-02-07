# 숫자는 무작위로 입력해도 상관 없습니다.
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else: 
        counter[number] = 1

# 최종 출력
print(counter)
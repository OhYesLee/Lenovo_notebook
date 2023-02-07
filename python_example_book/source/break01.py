# 변수를 선언합니다.
numbers = [5, 15, 6, 20, 7, 25]

# 반복을 돌립니다.
for number in numbers:
    # number가 10보다 작으면 다음 반복으로 넘어갑니다.
    if number < 10:
        continue
    # 출력합니다.
    print(number)

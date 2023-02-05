# 함수를 선언합니다.
def sum_all(start=0, end=100, step=1):
    # 변수를 선언합니다.
    output = 0
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start, end + 1, step):
        output += i
    # 리턴합니다.
    return output

# 함수를 호출합니다.
print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))
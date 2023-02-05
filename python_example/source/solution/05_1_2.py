def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output

# 함수를 호출합니다.
print(mul(5, 7, 9, 10))
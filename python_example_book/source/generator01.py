# 함수를 선언합니다.
def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
	
# 함수를 호출합니다.
output = test()
	
# next() 함수를 호출합니다.
print("D 지점 통과")
a = next(output)
print(a)
	
print("E 지점 통과")
b = next(output)
print(b)

print("F 지점 통과")
c = next(output)
print(c)

# 한번 더 실행하기
next(output)
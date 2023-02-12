import time


''' 실행 시간 측정 데코레이터 '''
def elapsed(func):                                     # 함수를 인풋으로 받는다.
    def wrapper(a, b):
        print('함수가 실행됩니다.')
        start = time.time()
        result = func(a, b)                            # 함수 실행
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 함수 수행시간
        return result                                  # 함수 실행 결과 반환
    return wrapper


@elapsed
def func1(a, b):
    val = a + b
    return val

@elapsed
def func2(a, b):
    val = a * b
    return val


if __name__ == "__main__":
    func1(1,2)
    func2(1, 2)
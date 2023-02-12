def isLeapYear(year):  # 윤년이면 True, 아니면 False 를 출력하는 함수.
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def lastDay(year, month):  # 인수로 년, 월을 넘겨받아 그 달의 마지막 날짜를 리턴하는 함수
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 12달의 마지막 날짜를 기억하는 리스트를 만든다. => 일단 2월의 마지막 날짜는 28일로 초기화 시킨다.

    # 2월의 마지막 날짜를 확정한다. => 윤년이면 29일로 수정한다.
    # if isLeapYear(year):
    # m[1] = 29
    m[1] = 29 if isLeapYear(year) else 28  # isLeapYear(year)이 T이면 m[1]은 29이다.    

    return m[month - 1]  # 인수로 넘겨받은 월에 해당되는 마지막 날짜를 리턴시킨다.


def totalDay(year, month, day):  # 년, 월, 일을 넘겨받아 1년 1월 1일 부터 지난 날짜의 합계를 리턴하는 함수
    # 1년 1월 1일 부터 전 년도 12월 31일 까지 지난 날짜를 계산한다.
    total = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    # 전년도 까지 지난 날짜의 합계에 전 달까지 지난 날짜를 더한다.
    for i in range(1, month):  # i가 1부터 month까지 변하는 동안.
        total += lastDay(year, i)  # m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]의 성분들을 통해 계산 된다.

    return total + day  # 전달 까지 지난 날짜에 일을 더해서 리턴시킨다.


def weekDay(year, month, day):
    return totalDay(year, month, day) % 7

    # 인수로 년, 월, 일을 넘겨받아 요일을 계산해 숫자로 리턴하는 함수
    # 일요일(0), 월요일(1), 화요일(2), 수요일(3), 목요일(4), 금요일(5), 토요일(6)


if __name__ == "__main__":
    year, month = map(int, input('달력을 출력할 년, 월을 입력하세요 : ').split())
    print('=' * 28)
    print('         {0:4d}년{1:2d}월'.format(year, month))
    print('=' * 28)
    print(' 일  월  화  수  목  금  토 ')
    print('=' * 28)  # 여기까진 달력의 윗부분이다.

    for i in range(weekDay(year, month, 1)):
        # 1일이 출력될 요일의 위치를 맞추기 위해서 1일의 요일만큼 반복하며 빈칸을 출력한다.
        print('    ', end = '')  # 빈 칸은 반복당 4칸씩 띄운다.

    # 1일 부터 달력을 출력할 달의 마지막 날짜까지 반복하며 달력을 출력한다.
    for i in range(1, lastDay(year, month) + 1):  # i가 1부터 해당 달의 마지막 날짜의 수까지 변하는 동안.
        print(' {0:2d} '.format(i), end = '')

        # 출력한 날짜(i)가 토요일이고 그 달의 마지막 날짜가 아니면 줄을 바꾼다.
        if weekDay(year, month, i) == 6 and i != lastDay(year, month):
            print()

    print('\n' + '=' * 28)  # 달력 하단 부분.
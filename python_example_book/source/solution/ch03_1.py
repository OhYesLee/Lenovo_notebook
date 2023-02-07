import datetime

입력 = input("입력: ")

if "안녕" in 입력:
    print("안녕하세요.")
elif "몇 시" in 입력:
    now = datetime.datetime.now()
    print(f"지금은 {now.hour}시입니다.")
else:
    print(입력)
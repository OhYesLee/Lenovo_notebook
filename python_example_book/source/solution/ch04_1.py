a = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
counter = {}
for i in a:
    if i not in counter:
        counter[i] = 0
    counter[i] += 1
    
print(f"{a}에서")
print(f"사용된 숫자의 종류는 {len(counter)}개입니다.")
print()
print(f"참고: {counter}")
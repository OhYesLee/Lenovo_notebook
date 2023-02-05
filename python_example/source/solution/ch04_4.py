a = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
output = []

for i in a:
    if type(i) == list:
        # 요소가 리스트라면: 또 반복해서 요소를 추가합니다.
        for j in i:
            output.append(j)
    else:
        # 요소가 숫자라면: 그냥 추가합니다.
        output.append(i)
    
print(f"{a}를 평탄화하면")
print(f"{output}입니다")
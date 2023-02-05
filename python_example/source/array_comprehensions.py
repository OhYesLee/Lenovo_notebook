# 리스트를 선언합니다.
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit
    for fruit in array
    if fruit != "초콜릿"]

# 출력합니다.
print(output)
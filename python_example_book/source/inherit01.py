# 부모 클래스를 선언합니다.
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메서드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메서드입니다.")

# 자식 클래스를 선언합니다.
class Child(Parent):
    def __init__(self):
        super().__init__() # 부모의 __init__() 함수를 호출합니다.
        print("Child 클래스의 __init()__ 메서드가 호출되었습니다.")

# 자식 클래스의 인스턴스를 생성하고 부모의 메서드를 호출합니다.
child = Child()
child.test()
print(child.value)
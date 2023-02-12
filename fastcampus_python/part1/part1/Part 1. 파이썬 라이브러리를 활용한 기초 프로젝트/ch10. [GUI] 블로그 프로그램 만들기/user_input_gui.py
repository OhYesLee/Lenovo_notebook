from tkinter import *

def btn_click(event):
    print(f"사용자 입력 값은 : \n{text.get(1.0, END)} 입니다 !")

data = '''여러줄의 데이터를 입력하고 버튼을 클릭해주세요'''

root = Tk()
root.geometry('500x500')

text = Text(root)                             # root 창에 Text 컴포넌트(위젯) 추가
text.insert(1.0, data)                        # 첫번째 데이터에 Text 입력값 저장
text.pack()                                   # Text 객체를 창에 표시

b1 = Button(root, text='결과값 확인')         # root 창에 Text 컴포넌트(위젯) 추가
b1.bind('<Button-1>', btn_click)              # Button 클릭 시  btn_click 함수 호출
b1.pack()

root.mainloop()
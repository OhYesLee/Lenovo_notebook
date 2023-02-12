from tkinter import *
from tkinter.messagebox import *
from blog_data_model import *

root = Tk()                                   # tkinter 객체(창) 생성
root.title('나만의 블로그')                    # 제목 입력

# 컴포넌트 생성
listbox = Listbox(root, exportselection=False)    # 블로그 목록을 표시할 리스트 박스
label = Label(root, text='제목')                  # '제목' 문자열을 표시할 라벨
entry = Entry(root)                               # 제목에 해당하는 내용을 표시할 엔트리
text = Text(root)                                 # 블로그 내용을 표시할 텍스트
b1 = Button(root, text='생성')
b2 = Button(root, text='수정')
b3 = Button(root, text='삭제')

# 컴포넌트 배치
listbox.grid(row=0, column=0, columnspan=3, sticky='ew')
label.grid(row=1, column=0)

entry.grid(row=1, column=1, columnspan=2, sticky='ew')
text.grid(row=2, column=0, columnspan=3)
b1.grid(row=3, column=0, sticky='ew')
b2.grid(row=3, column=1, sticky='ew')
b3.grid(row=3, column=2, sticky='ew')


# 블로그 행 인덱스 저장 리스트
ROW_IDS = []



def load_blog_list():
    listbox.delete(0, END)  # 리스트 박스 초기화
    blog_list = get_blog_list()  # 블로그 리스트 가져오기

    for i, blog in enumerate(blog_list):
        print(blog)
        ROW_IDS.append(blog[0])  # 블로그 행 인덱스(ID) 저장
        listbox.insert(i, '[%s/%s/%s] %s' % (
            blog[3][:4], blog[3][4:6], blog[3][6:], blog[1]))  # 리스트 박스에 추가

def refresh():
    ROW_IDS.clear()        # 블로그 ID 리스트 삭제
    entry.delete(0, END)   # 제목 삭제
    text.delete(1.0, END)  # 내용 삭제
    load_blog_list()       # 블로그 리스트 불러오기

def get_blog(event):
    _id = ROW_IDS[listbox.curselection()[0]]  # 마우스 커서가 선택한 요소의 위치(인덱스) 반환
    blog = read_blog(_id)  # 해당 위치 블로그 읽기
    entry.delete(0, END)
    entry.insert(0, blog[1])  # 엔트리에 제목 추가
    text.delete(1.0, END)
    text.insert(1.0, blog[2])  # 텍스트에 내용 추가


listbox.bind('<<ListboxSelect>>', get_blog)  # 리스트 박스에 get_blog 함수 바인딩


def btn_add(event):
    subject = entry.get().strip()  # 엔트리(제목란)에 입력한 값
    content = text.get(1.0, END).strip()  # 텍스트(내용란)에 입력한 값

    if not subject or not content:  # 제목 또는 내용이 없을 시 오류창 발생
        showerror("오류", "제목 또는 내용을 입력해 주세요")
        return
    add_blog(subject, content)  # 블로그 추가
    refresh()

b1.bind('<Button-1>', btn_add)  # '생성' 버튼에 btn_add 함수 바인딩


def btn_modify(event):
    sel = listbox.curselection()  # 리스트 박스 선택 값 가져오기
    if not sel:  # 선택 값이 없을 경우
        showerror("오류", "리스트를 먼저 선택해 주세요")
    else:  # 선택 값이 있을 경우
        _id = ROW_IDS[sel[0]]
    subject = entry.get().strip()  # 엔트리(제목란)에 수정한 값
    content = text.get(1.0, END).strip()  # 텍스트(내용란)에 수정한 값

    if not subject or not content:  # 제목 또는 내용이 없을 시 오류창 발생
        showerror("오류", "제목 또는 내용을 입력해 주세요")
        return

    modify_blog(_id, subject, content)  # 블로그 수정
    refresh()

b2.bind('<Button-1>', btn_modify)  # '수정' 버튼에 btn_modify 함수 바인딩


def btn_remove(event):
    sel = listbox.curselection()  # 리스트 박스 선택 값 가져오기
    if not sel:
        showerror("오류", "리스트를 먼저 선택해 주세요")
        return
    else:
        _id = ROW_IDS[sel[0]]

    if askyesno("확인", "정말로 삭제하시겠습니까?"):  # 확인 창 발생
        remove_blog(_id)  # 블로그 삭제
        refresh()

b3.bind('<Button-1>', btn_remove)  # '삭제' 버튼에 btn_remove 함수 바인딩


load_blog_list()
root.mainloop()
import sqlite3
import pandas as pd



if __name__ == "__main__":

    # 쇼핑몰 데이터 베이스
    conn = sqlite3.connect("shopping_mall.db", isolation_level=None)

    # 커서 생성
    c = conn.cursor()

    product_list = pd.read_csv('product_list.csv', encoding='euc-kr')
    print(product_list)

    # 상품 리스트 테이블 추가
    product_list.to_sql('productList', conn, if_exists='append', index = False)

    # 주문 목록 추가
    c.execute(
        "CREATE TABLE IF NOT EXISTS orderList(ID INTEGER PRIMARY KEY AUTOINCREMENT, 상품명 TEXT, 개수 INTEGER, 가격 INTEGER, 총합 INTEGER)")
    conn.commit()

    while True:

        ## 상품 목록을 표시
        print("------------------상품목록------------------")
        for row in c.execute('SELECT ID, 상품명, 가격 FROM productList'):
            print('상품번호 :', row[0], ', 상품명 :', row[1], ', 가격 :', row[2])
        print("--------------------------------------------")

        ## 사용자 상품 선택
        print('')
        num = input("구매하실 상품의 번호를 입력해주세요: ")
        c.execute("SELECT 상품명, 가격 FROM productList WHERE id = ?", (num,))
        result = c.fetchone()

        ## 상품 번호와 주문 수량을 입력
        print('')
        count = int(input("구매할 수량을 입력해주세요: "))
        total = count * int(result[1])

        ## 주문 데이터를 db에 추가
        c.execute("INSERT INTO orderList (상품명, 개수, 가격, 총합) VALUES (?,?,?,?)", (result[0], count, result[1], total))

        ## 현재까지 주문 내역을 출력
        print('')
        print("현재까지 구매한 내역 보기")
        print("--------------------주문목록--------------------")
        for row in c.execute('SELECT * FROM orderList'):
            print('상품명 :', row[1], ', 주문수량 :', row[2], ', 단가 :', row[3], ', 구매가격 :', row[4])
        print("------------------------------------------------")

        ## 사용자 추가 구매 여부
        print('')
        print("상품을 추가 구매하시겠습니까?\n중단하려면 'x'을 눌러주세요.\n계속 하시려면 엔터키를 눌러주세요. ")
        if (input() == "x"): break


    ## 주문 내역에서 총 구매 가격 계산
    print("총 구매가격", end='')

    for row in c.execute('SELECT sum(총합) FROM orderList'):
        print(' : ',row[0],'원')
    print('')

    ## 주문 내역 초기화
    c.execute("DELETE FROM orderList")

    ## 데이터 베이스 연결 해제
    conn.close()
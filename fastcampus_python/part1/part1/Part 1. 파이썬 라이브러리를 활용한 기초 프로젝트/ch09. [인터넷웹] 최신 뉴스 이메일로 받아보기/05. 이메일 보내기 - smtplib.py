# 발송할 메세지는 email 모듈을 사용해서 작성
import smtplib
from email.mime.multipart import MIMEMultipart
import os
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import getpass


#  파일 첨부용 멀티파트 객체
msg = MIMEMultipart()

# 이메일 송수신자 설정
msg['From'] = '송신자 이메일 주소'
msg['To'] = '수신자 이메일 주소'

# 날짜 설정
from email.utils import formatdate
msg['Date'] = formatdate(localtime=True)  # 현재 지역에 맞는 날짜
msg['Date']

# 이메일 제목/본문 작성
from email.header import Header
from email.mime.text import MIMEText
msg['Subject'] = Header(s='파일첨부 메일송신 테스트', charset='utf-8')
body = MIMEText('첨부된 파일 2개를 확인해 주세요.', _charset='utf-8')

# 메일 본문 추가
msg.attach(body)

# 파일 첨부하기
files = list()
files.append('test1.pdf')
files.append('test2.jpg')

for f in files:
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(f, "rb").read())
    encode_base64(part)                           # 바이너리 파일 base64 인코딩
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)                              # 파일 첨부



mailServer = smtplib.SMTP_SSL('smtp.gmail.com')           # SMTP 서버를 사용한 메세지 발송
mailServer.login('이메일주소', getpass.getpass())          # 본인 계정과 비밀번호 사용 (Gmail : 앱 비밀번호)
mailServer.send_message(msg)
mailServer.quit()
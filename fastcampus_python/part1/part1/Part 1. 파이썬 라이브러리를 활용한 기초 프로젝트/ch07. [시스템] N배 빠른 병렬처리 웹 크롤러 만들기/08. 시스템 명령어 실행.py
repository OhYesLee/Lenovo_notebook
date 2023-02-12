import subprocess
subprocess.run(['python', 'test.py'])

# # 출력 결과를 txt 파일로 저장
# f = open('output.txt', 'w')
# out = subprocess.check_output(['python', 'test.py'], encoding='utf-8')
# f.write(out)
# f.close()
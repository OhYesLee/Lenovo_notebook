import random
f = open("voca.txt","r",encoding='UTF-8')
raw_data = f.read()
f.close()
print(raw_data.split("\n")[-1])
data_list = raw_data.split("\n")
data_list = data_list[:-1]
while True:
    r_index = random.randrange(0,len(data_list))
    word = data_list[r_index].replace(u"\xa0", u" ").split(" ")[1]
    if len(word) <= 6 :break
print(word)
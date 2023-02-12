import pygame
# 1. 게임 초기화
pygame.init()
# 2. 게임창 옵션 설정
size = (500, 1000)
screen = pygame.display.set_mode(size)
title = "새똥 피하기"
pygame.display.set_caption(title)
# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)
def img_read(file_name, resize):
    img = pygame.image.load(file_name+".png")
    img_size = img.get_size()
    img_size = (img_size[0]*resize, img_size[1]*resize)
    img = pygame.transform.smoothscale(img,img_size)
    return img
person_static = img_read("man_static",0.15)
person_size = person_static.get_size()
p_list = [img_read("man_0",0.15),img_read("man_1",0.15),img_read("man_2",0.15),
          img_read("man_3",0.15),img_read("man_2",0.15),img_read("man_1",0.15)]
class person:
    def __init__(self):
        self.img = person_static
        self.size = self.img.get_size()
        self.pos = tup_r((size[0]/2-self.size[0]/2,size[1]-self.size[1]))
    def show(self):
        screen.blit(self.img, self.pos)
        
player = person()
k = 0
exit = False
# 4. 메인 이벤트
while not exit:
    # 4-1. FPS 설정
    clock.tick(60)
    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    # 4-3. 입력, 시간에 따른 변화
    k += 0.2
    kk = int(k) % 6
    player.img = p_list[kk]
    # 4-4. 그리기
    screen.fill(white)
    player.show()
    # 4-5. 업데이트
    pygame.display.flip()
# 5. 게임 종료
pygame.quit()
import pygame, random
# 1. 게임 초기화
pygame.init()
# 2. 게임창 옵션 설정
size = (1000, 1000)
screen = pygame.display.set_mode(size)
title = "MOLECATCH"
pygame.display.set_caption(title)
# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
x_list = [163,500,830]
y_list = [248,580,916]
def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)
bg_img = pygame.image.load("bg.png")
bg_img = pygame.transform.smoothscale(bg_img, size)
mole_img1 = pygame.image.load("mole_1.png")
mole_img2 = pygame.image.load("mole_2.png")
mole_size = mole_img1.get_size()
mole_size = tup_r((mole_size[0]*0.2, mole_size[1]*0.2))
mole_img1 = pygame.transform.smoothscale(mole_img1, mole_size)
mole_img2 = pygame.transform.smoothscale(mole_img2, mole_size)
hammer_img1 = pygame.image.load("hammer.png")
hammer_size = hammer_img1.get_size()
hammer_size = tup_r((hammer_size[0]*0.15, hammer_size[1]*0.15))
hammer_img1 = pygame.transform.smoothscale(hammer_img1, hammer_size)
hammer_img2 = pygame.transform.rotate(hammer_img1, 90)
hammer_img = hammer_img1
hammer_stage = 0 # 0 :직립 1: 회전
hammer_staytime = 100
game_point = 0
game_time = 10000
point_font = pygame.font.Font("C:/Windows/Fonts/BMDOHYEON_ttf.ttf", 30)
t_font = point_font

# 두더지 class
class mole:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.img = mole_img1
        self.crop = 0
        self.move = 10
        self.stage = 0
        self.staytime = 200
        self.clicked = False
        self.size = mole_size
    
    def crop_change(self):
        if self.stage == 0:
            if random.random() < 0.1 : self.stage = 1
        elif self.stage == 1:
            self.crop += self.move
            if self.crop >= self.size[1] : 
                self.crop = self.size[1]
                self.stage = 2
                self.stay_start = now_time
        elif self.stage == 2:
            if now_time - self.stay_start >= self.staytime :
                self.stage = 3
        elif self.stage == 3:
            self.crop -= self.move
            if self.crop <= 0 : 
                self.crop = 0
                self.stage = 0
                self.img = mole_img1
                self.clicked = False
        self.img_cropped = self.img.subsurface((0,0,self.size[0],self.crop))
        self.pos = tup_r((x_list[self.i]-self.size[0]/2, y_list[self.j]-self.crop))
        self.range = (self.pos[0], self.pos[1], self.size[0], self.crop)
    
   
    def show(self):
        screen.blit(self.img_cropped, self.pos)

mole_list = []
for i in range(3):
    for j in range(3):
        aa = mole(i, j)
        mole_list.append(aa)        
  
click_go = False
exit = False
# 4. 메인 이벤트
game_start_time = pygame.time.get_ticks()
while not exit:
    # 4-1. FPS 설정
    clock.tick(60)
    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_go = True

    # 4-3. 입력, 시간에 따른 변화
    now_time = pygame.time.get_ticks()
    x, y = pygame.mouse.get_pos()
    total_time = round((game_time - (now_time - game_start_time))/1000)

    if hammer_stage == 0:
        hammer_pos = (x, y-hammer_size[1])
        if click_go == True:
            hammer_stage = 1
            hammer_stay_start = now_time
            hammer_img = hammer_img2
    elif hammer_stage == 1:
        hammer_pos = (x-50, y-hammer_size[1]+50)     
        if now_time - hammer_stay_start >= hammer_staytime :
            hammer_stage = 0
            hammer_img = hammer_img1
            
    for mole in mole_list:
        mole.crop_change()
    
    if click_go == True :
        for mole in mole_list:
            if mole.clicked == False:
                x1, y1, w, h = mole.range
                if x >= x1 and x <= x1+w and y >= y1 and y <= y1+h:
                    mole.clicked = True
                    mole.stage = 3
                    mole.img = mole_img2
                    game_point += 1
        click_go = False        

    # 4-4. 그리기
    screen.blit(bg_img, (0,0))
    for mole in mole_list:
        mole.show()
    screen.blit(hammer_img, hammer_pos)
    # 점수 표시
    point = point_font.render(f"점수 : {game_point}", True, black)
    point_size = point.get_size()
    point_pos = (20, 20)
    screen.blit(point, point_pos)
    # 시간 표시
    t = t_font.render(f"남은 시간 : {total_time}", True, black)
    t_size = t.get_size()
    t_pos = (size[0]-20-t_size[0], 20)
    screen.blit(t, t_pos)        
    # 4-5. 업데이트
    pygame.display.flip()
# 5. 게임 종료
pygame.quit()
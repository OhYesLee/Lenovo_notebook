import pygame, math, random
# 1. 게임 초기화
pygame.init()
# 2. 게임창 옵션 설정
size = (800, 1000)
screen = pygame.display.set_mode(size)
title = "새똥 피하기"
pygame.display.set_caption(title)
# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
def sound_read(file_name):
    sound = pygame.mixer.Sound(f"{file_name}.ogg")
    sound.set_volume(0.2)
    return sound
sound_drop = sound_read("drop")
sound_sad = sound_read("sad") 
sound_sad.set_volume(0.5)
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
person_static = img_read("char_static",0.15)
person_dead = img_read("char_dead",0.15)
person_size = person_static.get_size()
p_list = [img_read("char_0",0.15),img_read("char_1",0.15),img_read("char_2",0.15),
          img_read("char_3",0.15)]
b_r = 0.15
b_list = [[img_read("bird_0_0",b_r), img_read("bird_0_1",b_r),img_read("bird_0_2",b_r),img_read("bird_0_3",b_r),img_read("bird_0_2",b_r),img_read("bird_0_1",b_r)],
          [img_read("bird_1_0",b_r), img_read("bird_1_1",b_r),img_read("bird_1_2",b_r),img_read("bird_1_3",b_r),img_read("bird_1_2",b_r),img_read("bird_1_1",b_r)],
          [img_read("bird_2_0",b_r), img_read("bird_2_1",b_r),img_read("bird_2_2",b_r),img_read("bird_2_3",b_r),img_read("bird_2_2",b_r),img_read("bird_2_1",b_r)]]
dung_img = img_read("dung",0.15)
class person:
    def __init__(self):
        self.img = person_static
        self.size = self.img.get_size()
        self.pos = tup_r((size[0]/2-self.size[0]/2,size[1]-self.size[1]))
        self.move = 10
        self.timer = 0
        self.ani_move = 0.2
    def show(self):
        screen.blit(self.img, self.pos)
class bird:
    def __init__(self):
        self.timer = 0
        self.ani_move = 0.2        
        self.index = random.randrange(0, 3)
        self.img = b_list[self.index][0]
        self.size = self.img.get_size()
        self.drop_x = random.randrange(100,size[0]-100-self.size[0])
        self.drop = False
        self.create_x = size[0]
        self.create_y = random.randrange(200,500)
        self.target_x = -self.size[0]
        self.target_y = random.randrange(200,500)
        if random.random() > 0.5 :
            self.create_x, self.target_x = self.target_x, self.create_x
        self.dx = self.target_x - self.create_x
        self.dy = self.target_y - self.create_y
        self.dd = (self.dx**2+self.dy**2)**0.5
        self.pos = (self.create_x, self.create_y)
        self.move = random.randrange(2, 10)
        self.move_x = self.move * self.dx/self.dd
        self.move_y = self.move * self.dy/self.dd
        self.angle = math.atan(abs(self.dy/self.dx))*180/math.pi
    def show(self):
        screen.blit(self.img, self.pos)
class dung:
    def __init__(self, x, y, move_x):
        self.pos = x, y
        self.move_x = move_x
        self.move_y = 2
        self.a_y = 0.3
        self.img = dung_img
        self.size = self.img.get_size()
    def show(self):
        screen.blit(self.img, self.pos)

point_font = pygame.font.Font("C:/Windows/Fonts/BMDOHYEON_ttf.ttf", 50)
finalp_font = pygame.font.Font("C:/Windows/Fonts/BMDOHYEON_ttf.ttf", 80)
        
player = person()
bb_list = []
dd_list = []

game_over = False
left_go = False
right_go = False
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
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name == "left":
                left_go = True
            elif key_name == "right":
                right_go = True
        if event.type == pygame.KEYUP:
            key_name = pygame.key.name(event.key)
            if key_name == "left":
                left_go = False
                player.timer = 0
            elif key_name == "right":
                right_go = False
                player.timer = 0
    # 4-3. 입력, 시간에 따른 변화
    now_time = pygame.time.get_ticks()
    if game_over == False:
        total_time = now_time - game_start_time
    # 새 생성
    if random.random() < 0.05:
        bb = bird()
        bb_list.append(bb)
    # 플레이어 움직임
    if game_over == True:
        player.img = person_dead  
    else:  
        if left_go == True and right_go == False:
            player.pos = (player.pos[0]-player.move, player.pos[1])
            player.timer += player.ani_move
            player.img = p_list[int(player.timer)%len(p_list)]
            player.img = pygame.transform.flip(player.img, True, False)
            if player.pos[0] <= 0:
                player.pos = (0, player.pos[1])
        elif left_go == False and right_go == True:
            player.pos = (player.pos[0]+player.move, player.pos[1])
            player.timer += player.ani_move
            player.img = p_list[int(player.timer)%len(p_list)]
            if player.pos[0] >= size[0]-player.size[0]:
                player.pos = (size[0]-player.size[0], player.pos[1]) 
        else : player.img = person_static

    # 새 움직임
    for bb in bb_list:
        bb.timer += bb.ani_move
        bb.img = b_list[bb.index][int(bb.timer)%len(b_list[bb.index])]
        if bb.move_x > 0 : 
            bb.img = pygame.transform.flip(bb.img, True, False)
        if bb.dx*bb.dy < 0:
            bb.img = pygame.transform.rotate(bb.img, bb.angle)
        else:
            bb.img = pygame.transform.rotate(bb.img, -bb.angle)    
        bb.pos = (bb.pos[0]+bb.move_x, bb.pos[1]+bb.move_y)
        if bb.move_x > 0 : # 왼쪽에서 오른쪽
            if bb.pos[0] >= bb.drop_x and bb.drop == False:
                dd = dung(round(bb.pos[0]+bb.size[0]/2), bb.pos[1]+bb.size[1], bb.move_x)
                dd_list.append(dd)
                bb.drop = True
        else : # 오른쪽에서 왼쪽
            if bb.pos[0] <= bb.drop_x and bb.drop == False:
                dd = dung(round(bb.pos[0]+bb.size[0]/2), bb.pos[1]+bb.size[1], bb.move_x)
                dd_list.append(dd)
                bb.drop = True  
    # 새똥 움직임
    for dd in dd_list:
        dd.move_y += dd.a_y
        dd.pos = (dd.pos[0]+dd.move_x , dd.pos[1]+dd.move_y)   
        X, Y = player.pos
        W, H = player.size
        x, y = dd.pos
        w, h = dd.size
        if X-w<x and x<X+W and Y-h<y and y<Y+H-h and game_over == False:
            game_over = True
            sound_sad.play()
    # 새 소멸
    del_list = []
    for i, bb in enumerate(bb_list):     
        if bb.pos[0] < -bb.size[0] or bb.pos[0] > size[0]:
            del_list.append(i)
    del_list.reverse()
    for i in del_list:
        del bb_list[i]
    # 새똥 소멸
    play_go = False
    del_list = []
    for i, dd in enumerate(dd_list):     
        if dd.pos[1] > size[1]-dd.size[1]:
            del_list.append(i)
            play_go = True
    del_list.reverse()
    for i in del_list:
        del dd_list[i]
    if play_go == True and game_over == False:
        sound_drop.play()
    # 4-4. 그리기
    screen.fill(white)
    player.show()
    for bb in bb_list:
        bb.show()
    for dd in dd_list:
        dd.show()
    # 점수 표시
    point_img = point_font.render(str(total_time/1000), True, black)
    point_size = point_img.get_size()
    point_pos = (325, 20)
    screen.blit(point_img, point_pos)
    # 종료 화면
    if game_over == True:
        finish_bg = pygame.Surface(size)
        finish_bg.fill(black)
        finish_bg.set_alpha(200)
        screen.blit(finish_bg, (0,0))
        finalp_img = finalp_font.render(f"최고 기록 : {total_time/1000}", True, white)
        finalp_size = finalp_img.get_size()
        finalp_pos = tup_r((size[0]/2-finalp_size[0]/2, size[1]/3-finalp_size[1]/2))
        finalp2_img = finalp_font.render(f"현재 기록 : {total_time/1000}", True, white)
        finalp2_size = finalp2_img.get_size()
        finalp2_pos = tup_r((size[0]/2-finalp2_size[0]/2, 100+size[1]/3-finalp2_size[1]/2+finalp2_size[1]))        
        screen.blit(finalp_img, finalp_pos)        
        screen.blit(finalp2_img, finalp2_pos)                   
    # 4-5. 업데이트
    pygame.display.flip()
# 5. 게임 종료
pygame.quit()
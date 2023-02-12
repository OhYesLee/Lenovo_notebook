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
mole_size = tup_r((mole_size[0]*0.25, mole_size[1]*0.25))
mole_img1 = pygame.transform.smoothscale(mole_img1, mole_size)
mole_img2 = pygame.transform.smoothscale(mole_img2, mole_size)
mole_img = mole_img1
mole_crop = 0
mole_move = 10
mole_stage = 0
mole_staytime = 200
mole_clicked = False
click_go = False
exit = False
# 4. 메인 이벤트
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
    if mole_stage == 0:
        if random.random() < 0.1 : mole_stage = 1
    elif mole_stage == 1:
        mole_crop += mole_move
        if mole_crop >= mole_size[1] : 
            mole_crop = mole_size[1]
            mole_stage = 2
            mole_stay_start = now_time
    elif mole_stage == 2:
        if now_time - mole_stay_start >= mole_staytime :
            mole_stage = 3
    elif mole_stage == 3:
        mole_crop -= mole_move
        if mole_crop <= 0 : 
            mole_crop = 0
            mole_stage = 0
            mole_img = mole_img1
            mole_clicked = False
    mole_img_cropped = mole_img.subsurface((0,0,mole_size[0],mole_crop))
    mole_pos = tup_r((x_list[0]-mole_size[0]/2, y_list[0]-mole_crop))
    mole_range = (mole_pos[0], mole_pos[1], mole_size[0], mole_crop)
    if click_go == True and mole_clicked == False:
        x, y = pygame.mouse.get_pos()
        x1, y1, w, h = mole_range
        if x >= x1 and x <= x1+w and y >= y1 and y <= y1+h:
            mole_clicked = True
            mole_stage = 3
            mole_img = mole_img2
        click_go = False
    # 4-4. 그리기
    screen.blit(bg_img, (0,0))
    screen.blit(mole_img_cropped, mole_pos)
    # 4-5. 업데이트
    pygame.display.flip()
# 5. 게임 종료
pygame.quit()
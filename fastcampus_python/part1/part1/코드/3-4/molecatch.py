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
mole_img = pygame.image.load("mole_1.png")
mole_size = mole_img.get_size()
mole_size = tup_r((mole_size[0]*0.25, mole_size[1]*0.25))
mole_img = pygame.transform.smoothscale(mole_img, mole_size)
mole_crop = 0
mole_move = 5
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
            print(pygame.mouse.get_pos())
    # 4-3. 입력, 시간에 따른 변화
    mole_crop += mole_move
    if mole_crop >= mole_size[1] : mole_crop = mole_size[1]
    mole_img_cropped = mole_img.subsurface((0,0,mole_size[0],mole_crop))
    mole_pos = tup_r((x_list[0]-mole_size[0]/2, y_list[0]-mole_crop))
    # 4-4. 그리기
    screen.blit(bg_img, (0,0))
    screen.blit(mole_img_cropped, mole_pos)
    # 4-5. 업데이트
    pygame.display.flip()
# 5. 게임 종료
pygame.quit()
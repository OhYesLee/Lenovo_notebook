import pygame, math, random

# 1. 게임 초기화
pygame.init()
# 2. 게임창 옵션 설정
size = [500,900]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("HANGMAN")
# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
hint_font = pygame.font.Font("C:/Windows/Fonts/BMDOHYEON_ttf.ttf", 80)
entry_font = pygame.font.Font("C:/Windows/Fonts/BMDOHYEON_ttf.ttf", 60)
no_font = pygame.font.Font("C:/Windows/Fonts/BMDOHYEON_ttf.ttf", 40)
title_font = pygame.font.Font("C:/Windows/Fonts/BMDOHYEON_ttf.ttf", 80)
guide_font = pygame.font.Font("C:/Windows/Fonts/BMDOHYEON_ttf.ttf", 20)
finish_font = pygame.font.Font("C:/Windows/Fonts/BMDOHYEON_ttf.ttf", 30)
sound_bad = pygame.mixer.Sound("bad.ogg")
sound_good = pygame.mixer.Sound("good.ogg")
sound_clock = pygame.mixer.Sound("clock.ogg")
sound_save = pygame.mixer.Sound("save.ogg")
sound_fail = pygame.mixer.Sound("fail.ogg")
sound_bad.set_volume(0.2)
sound_good.set_volume(0.2)
sound_clock.set_volume(0.2)
sound_save.set_volume(0.2)
sound_fail.set_volume(0.2)
def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)
exit = False
while not exit:
    entry_text = ""
    drop = False
    enter_go = False
    ready = False
    game_over = False
    save = False
    play_again = False

    #  A가 영어 단어를 1개 생각한다.
    f = open("voca.txt","r",encoding='UTF-8')
    raw_data = f.read()
    f.close()
    data_list = raw_data.split("\n")
    data_list = data_list[:-1]
    while True:
        r_index = random.randrange(0,len(data_list))
        word = data_list[r_index].replace(u"\xa0", u" ").split(" ")[1]
        if len(word) <= 6 :break
    word = word.upper()
    
    #  단어의 글자 수만큼 밑줄을 긋는다.
    word_show = "_"*len(word)
    try_num = 0
    ok_list = []
    no_list = []

    k = 0
    # 시작 화면
    sound_save.stop()
    sound_fail.stop()
    while not exit:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True   
            if event.type == pygame.KEYDOWN:
                ready = True
        if ready == True: break             
        screen.fill(black)
        title = title_font.render("HANGMAN", True, white)
        title_size = title.get_size()
        title_pos = tup_r((size[0]/2-title_size[0]/2, size[1]/2-title_size[1]/2))
        screen.blit(title, title_pos)
        guide = guide_font.render("PRESS ANY KEY TO START THE GAME", True, white)
        guide_size = guide.get_size()
        guide_pos = tup_r((size[0]/2-guide_size[0]/2, size[1]*4/5-guide_size[1]/2))
        if pygame.time.get_ticks() % 1000 > 500 :
            screen.blit(guide, guide_pos)    
        pygame.display.flip()
        
    # 4. 메인 이벤트
    sound_clock.play(-1)
    while not exit:
        # 4-1. FPS 설정
        clock.tick(60)
        # 4-2. 각종 입력 감지
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYDOWN:
                if drop == False and try_num == 8: # 빨간줄이 길어지는 동안
                    continue
                if game_over == True: play_again = True
                key_name = pygame.key.name(event.key)
                if (key_name == "return" or key_name == "enter"):
                    if entry_text != "" and (ok_list+no_list).count(entry_text) == 0 :
                        enter_go = True            
                elif len(key_name) == 1:
                    if (ord(key_name) >= 65 and ord(key_name) <= 90) or (ord(key_name) >= 97 and ord(key_name) <= 122):
                        entry_text = key_name.upper()
                    else : entry_text = ""
                else : entry_text = ""

        # 4-3. 입력, 시간에 따른 변화
        if play_again == True : break
        if try_num == 8 : k += 1
        if enter_go == True:
            ans = entry_text
            result = word.find(ans)
            if result == -1 : #없음
                try_num += 1
                no_list.append(ans)
                sound_bad.play()
            else : #있음
                ok_list.append(ans)
                for i in range(len(word)):
                    if word[i] == ans:
                        word_show = word_show[:i] + ans + word_show[i+1:]
                sound_good.play()
            enter_go = False
            entry_text = ""
        if drop == True: # 실패로 종료
            game_over = True
            word_show = word
            sound_clock.stop()
            
        if word_show.find("_") == -1 and game_over == False : # 성공으로 종료
            game_over = True
            save = True
            sound_clock.stop()
            sound_save.play()
        # 4-4. 그리기
        screen.fill(black)
        A = tup_r((0, size[1]*2/3))
        B = (size[0], A[1])
        C = tup_r((size[0]/6 , A[1]))
        D = (C[0], C[0])
        E = tup_r((size[0]/2, D[1]))
        if save != True:
            pygame.draw.line(screen, white, A, B, 3)
            pygame.draw.line(screen, white, C, D, 3)
            pygame.draw.line(screen, white, D, E, 3)
        F = tup_r((E[0], E[1]+size[0]/6))
        if drop == False and save != True:
            pygame.draw.line(screen, white, E, F, 3)
        r_head = round(size[0]/12)
        if drop == True : G = (F[0],F[1]+r_head+k*10)
        else : G = (F[0],F[1]+r_head)
        if try_num >= 1 or save == True: pygame.draw.circle(screen, white, G, r_head, 3)
        H = (G[0], G[1]+r_head)
        I = (H[0], H[1]+r_head)
        if try_num >= 2 or save == True:pygame.draw.line(screen, white, H, I, 3)
        l_arm = r_head*2
        J = (I[0]-l_arm*math.cos(30*math.pi/180),
            I[1]+l_arm*math.sin(30*math.pi/180))
        K = (I[0]+l_arm*math.cos(30*math.pi/180),
            I[1]+l_arm*math.sin(30*math.pi/180))
        J = tup_r(J)
        K = tup_r(K)
        if try_num >= 3 or save == True:pygame.draw.line(screen, white, I, J, 3)
        if try_num >= 4 or save == True:pygame.draw.line(screen, white, I, K, 3)
        L = (I[0], I[1]+l_arm)
        if try_num >= 5 or save == True:pygame.draw.line(screen, white, I, L, 3)
        l_leg = round(l_arm * 1.5)
        M = (L[0]-l_leg*math.cos(60*math.pi/180),
            L[1]+l_leg*math.sin(60*math.pi/180))
        N = (L[0]+l_leg*math.cos(60*math.pi/180),
            L[1]+l_leg*math.sin(60*math.pi/180))  
        M = tup_r(M)
        N = tup_r(N)  
        if try_num >= 6 or save == True:pygame.draw.line(screen, white, L, M, 3)
        if try_num >= 7 or save == True:pygame.draw.line(screen, white, L, N, 3)  
        if drop == False and try_num == 8:
            O = tup_r((size[0]/2-size[0]/6, E[1]/2+F[1]/2))
            P = (O[0]+k*2, O[1])
            if P[0] > size[0]/2+size[0]/6 :
                P = tup_r((size[0]/2+size[0]/6, O[1]))
                drop = True
                k = 0
                sound_fail.play()
            pygame.draw.line(screen, red, O, P, 3)
        # 힌트 표시하기
        hint = hint_font.render(word_show, True, white)
        hint_size = hint.get_size()
        hint_pos = tup_r((size[0]/2-hint_size[0]/2, size[1]*5/6-hint_size[1]/2))
        screen.blit(hint, hint_pos)
        # 입력창 표시하기
        entry = entry_font.render(entry_text, True, black)
        entry_size = entry.get_size()
        entry_pos = tup_r((size[0]/2-entry_size[0]/2, size[1]*17/18-entry_size[1]/2))
        entry_bg_size = 80
        pygame.draw.rect(screen, white, tup_r((size[0]/2-entry_bg_size/2, size[1]*17/18-entry_bg_size/2
                                        ,entry_bg_size ,entry_bg_size)))
        screen.blit(entry, entry_pos)
        # 오답 표시하기
        no_text = " ".join(no_list)
        no = no_font.render(no_text, True, red)
        no_pos = tup_r((20, size[1]*2/3+20))
        screen.blit(no, no_pos)
        # 종료 화면
        if game_over == True:
            finish_bg = pygame.Surface(size)
            finish_bg.fill(black)
            finish_bg.set_alpha(200)
            screen.blit(finish_bg, (0,0))
            if save == True: finish_text = "You saved the man"
            else : finish_text = "You killed the man"
            finish = finish_font.render(finish_text, True, white)
            finish_size = finish.get_size()
            finish_pos = tup_r((size[0]/2-finish_size[0]/2, size[1]*3/4-finish_size[1]/2))
            screen.blit(finish, finish_pos)
            guide = guide_font.render("PRESS ANY KEY TO PLAY AGAIN", True, white)
            guide_size = guide.get_size()
            guide_pos = tup_r((size[0]/2-guide_size[0]/2, size[1]*4/5-guide_size[1]/2))
            screen.blit(guide, guide_pos)          
        # 4-5. 업데이트
        pygame.display.flip()
# 5. 게임 종료
pygame.quit()
# 모듈 임포트
import pygame
import random

# 게임 변수 초기화
# 게임 화면
pygame.init()
size = [640, 640]
screen = pygame.display.set_mode(size)

# 시간관련 변수

try:
    # 그림과 효과음 삽입
    # 그림 삽입
    boy1_img = pygame.image.load("./img/boy_1.png")
    boy1_img = pygame.transform.scale(boy1_img, (40, 70))

    boy2_img = pygame.image.load("./img/boy_2.png")
    boy2_img = pygame.transform.scale(boy2_img, (60, 100))

    raindrop_img = pygame.image.load("./img/raindrop.png")
    raindrop_img = pygame.transform.scale(raindrop_img, (5, 20))

    white_raindrop_img = pygame.image.load("./img/white raindrop.png")
    white_raindrop_img = pygame.transform.scale(white_raindrop_img, (5, 20))

    gameover = pygame.image.load("./img/boy_failed.png")
    gameover = pygame.transform.scale(gameover, size)

    item_umbrella_img = pygame.image.load("./img/item_umbrella.png")
    item_umbrella_img = pygame.transform.scale(item_umbrella_img, (40, 40))

    item_lightningrod_img = pygame.image.load("./img/item_lightning rod.png")
    item_lightningrod_img = pygame.transform.scale(item_lightningrod_img, (40, 40))

    lightningrod_img = pygame.image.load("./img/lightningrod.png")
    lightningrod_img = pygame.transform.scale(lightningrod_img, (40, 40))

    item_potion_img = pygame.image.load("./img/item_potion.png")
    item_potion_img = pygame.transform.scale(item_potion_img, (40, 40))

    item_snowflake_img = pygame.image.load("./img/item_snowflake.png")
    item_snowflake_img = pygame.transform.scale(item_snowflake_img, (40, 40))

    snowflake_img = pygame.image.load("./img/snowflake.png")
    snowflake_img = pygame.transform.scale(snowflake_img, (20, 20))

    white_snowflake_img = pygame.image.load("./img/white_snowflake.png")
    white_snowflake_img = pygame.transform.scale(white_snowflake_img, (20, 20))

    hail_img = pygame.image.load("./img/hail.png")
    hail_img = pygame.transform.scale(hail_img, (30, 30))

    white_hail_img = pygame.image.load("./img/white_hail.png")
    white_hail_img = pygame.transform.scale(white_hail_img, (30, 30))

    coin_img = pygame.image.load("./img/coin.png")
    coin_img = pygame.transform.scale(coin_img, (25, 25))

    life_img = pygame.image.load("./img/life.png")
    life_img = pygame.transform.scale(life_img, (30, 30))

    splash_img = pygame.image.load("./img/splash.png")
    splash_img = pygame.transform.scale(splash_img, (20, 20))

    storm_start_img = pygame.image.load("./img/storm start image.png")
    storm_start_img = pygame.transform.scale(storm_start_img, size)

    thunder_img = pygame.image.load("./img/lightning.png")
    thunder_img = pygame.transform.scale(thunder_img, (10, 10))

    # background img
    background1 = pygame.image.load("./img/background_image/background_4.png")
    background1 = pygame.transform.scale(background1, (640, 640))

    background2 = pygame.image.load("./img/background_image/background_3.png")
    background2 = pygame.transform.scale(background2, (640, 640))

    background3 = pygame.image.load("./img/background_image/background_2.png")
    background3 = pygame.transform.scale(background3, (640, 640))

    background4 = pygame.image.load("./img/background_image/background_1.png")
    background4 = pygame.transform.scale(background4, (640, 640))

    # darkbackground img
    darkbackground1 = pygame.image.load("./img/darkbackground_image/darkbackground_4.png")
    darkbackground1 = pygame.transform.scale(darkbackground1, (640, 640))

    darkbackground2 = pygame.image.load("./img/darkbackground_image/darkbackground_3.png")
    darkbackground2 = pygame.transform.scale(darkbackground2, (640, 640))

    darkbackground3 = pygame.image.load("./img/darkbackground_image/darkbackground_2.png")
    darkbackground3 = pygame.transform.scale(darkbackground3, (640, 640))

    darkbackground4 = pygame.image.load("./img/darkbackground_image/darkbackground_1.png")
    darkbackground4 = pygame.transform.scale(darkbackground4, (640, 640))

    # 설명서
    dd = pygame.image.load("./img/dd.png")
    dd = pygame.transform.scale(dd, (640, 640))

    # 효과음 삽입
    takeoffsound = pygame.mixer.Sound("./sound/굿모닝 알람.mp3")
    landingsound = pygame.mixer.Sound("./audio/landing.wav")
    coinsound = pygame.mixer.Sound("./sound/coin_sound.mp3")
    coldsound = pygame.mixer.Sound("./sound/앗 차가워.mp3")
    diesound = pygame.mixer.Sound("./sound/으악.mp3")

except Exception as err:
    print('그림 또는 효과음 삽입에 문제가 있습니다.: ', err)
    pygame.quit()
    exit(0)

# 점수 출력
def text(s, arg, x, y):
    font = pygame.font.Font(None, 30)
    text = font.render(s + ':' + str(arg).zfill(6), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y
    screen.blit(text, textRect)

# 글자 출력
def textt(s, sizee, x, y):
    font = pygame.font.Font(None, sizee)
    textt = font.render(str(s), True, (0, 0, 0))
    texttRect = textt.get_rect()
    texttRect.left = x
    texttRect.top = y
    screen.blit(textt, texttRect)

position = screen.get_rect().centerx

def gamestart():
    startfpsClock = pygame.time.Clock()
    start_FPS = 30

    start_raindroptimer = 100
    start_raindrop_location = []
    start_speed_raindrop = 45

    while True:
        screen.blit(storm_start_img, (0, 0))
        start_raindroptimer -= 10
        if start_raindroptimer <= 0:
            start_raindrop_location.append([random.randint(5, size[1]), -30])
            start_raindroptimer = 1

            # 모든 start_raindrops 이동
        index = 0
        for start_raindrop in start_raindrop_location:
            start_raindrop[1] += start_speed_raindrop
            if start_raindrop[1] > size[1]:
                start_raindrop_location.pop(index)
            screen.blit(raindrop_img, (start_raindrop[0], start_raindrop[1]))
        startfpsClock.tick(start_FPS)
        running2 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # X 누르면 꺼진다
                pygame.quit()
                exit(0)
            # H 누르면 설명서가 나온다.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                running2 = True                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s and running2 == False: # s 누르면 시작
                    game()
            while running2:
                screen.fill((255,255,255))
                screen.blit(dd, (0,0))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                        running2 = False
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit(0)
            
        pygame.display.flip()

# 아이템 지속시간 출력
def timer(t, img):
    if t!=-1:
        screen.blit(img, (550, 90))
        textt(t, 24, 600, 100)
    
score_history = []

def game():
    # 게임 루프
    global max_score
    max_score = 0
    FPS = 50
    fpsClock = pygame.time.Clock()
    raindroptimer = 100
    hailtimer = 100
    v = 5
    speed_raindrop = 5
    speed_hail = 7
    speed_item = 4

    rodnumber = 0 # 현재 설치 가능한 보유한 피뢰침 개수
    rodblitlist = [] # 설치한 피뢰침들의 리스트

    start_thunder_time = -1

    boy_img = boy1_img
    falling_img = raindrop_img

    # 빗방울 위치, 시간 변수
    raindrop_location = []
    raindropaddingtime = 10

    # 우박 위치, 시간 변수
    hail_location = []
    hailaddingtime = 2
    
    # 아이템 위치 변수
    item_umbrella_location = []
    item_snowflake_location = []
    item_potion_location = []
    item_lightningrod_location = []

    # 아이템 시간 변수
    time_item_umbrella = -1
    time_item_snowflake = -1

    # splash 변수
    splash_location = []
    splash_location_floor = []
    splash_time = []
    splash_time_floor = []

    # 배경화면 바뀌는 변수
    backgroundnumber = 0

    # 배경화면 4개 변수
    b1 = background1
    b2 = background2
    b3 = background3
    b4 = background4

    # 빗방울 이미지 변수
    rdimg = raindrop_img

    # 눈 이미지 변수
    snimg = snowflake_img

    # 우박 이미지 변수
    haimg = hail_img

    # 점수
    score = 0

    start_life_location = 400
    lifenumber = 5
    
    running = True
    vec = 1.2
    flag = 0
    rodbbbpos=[]
    spacetime = []
    cnt=300
    check=True
    timezero = pygame.time.get_ticks()
    while running:
        # 화면을 그리기에 앞서 화면을 흰색으로 지우기
        screen.fill((255, 255, 255))

        #시간 정의
        wavetime=pygame.time.get_ticks() - timezero

        # wave 정의
        if 10000 < wavetime < 20000: # wave1
            wave = 1
            b1, b2, b3, b4 = darkbackground1, darkbackground2, darkbackground3, darkbackground4
            rdimg = white_raindrop_img
            snimg = white_snowflake_img
            haimg = white_hail_img
        elif 25000 <= wavetime < 35000: # wave2
            wave = 2
            b1, b2, b3, b4 = darkbackground1, darkbackground2, darkbackground3, darkbackground4
            rdimg = white_raindrop_img
            snimg = white_snowflake_img
            haimg = white_hail_img
        elif 40000 <= wavetime : # infinite wave
            wave = 3
            b1, b2, b3, b4 = darkbackground1, darkbackground2, darkbackground3, darkbackground4
            rdimg = white_raindrop_img
            snimg = white_snowflake_img
            haimg = white_hail_img
        else:
            wave = 0
            b1, b2, b3, b4 = background1, background2, background3, background4
            rdimg = raindrop_img
            snimg = snowflake_img
            haimg = hail_img

        # 키보드/마우스 이벤트
        for event in pygame.event.get():
            # X 버튼을 클릭하면 게임 종료
            if event.type == pygame.QUIT:
                exit()
            elif rodnumber != 0: # 피뢰침 아이템과 부딪혔다면
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # space 바 눌렀다면
                    rodbbbpos = boy_pos[:]
                    if boy_img == boy1_img:
                        rodbbbpos[1] += 40
                    elif boy_img == boy2_img:
                        rodbbbpos[1] += 70
                    rodblitlist.append(rodbbbpos)
                    rodnumber -= 1
                    spacetime.append(pygame.time.get_ticks())

        if backgroundnumber%4 == 0:
            screen.blit(b1, (0,0))
        elif backgroundnumber%4 == 1:
            screen.blit(b2, (0,0))
        elif backgroundnumber%4== 2:
            screen.blit(b3, (0,0))
        elif backgroundnumber%4 == 3:
            screen.blit(b4, (0,0))
        backgroundnumber += 1

        # wave 시작할 때 출력
        if 4000 < wavetime < 4800 or 5600 < wavetime < 6400 or 7000 < wavetime < 7600 or 8200 < wavetime < 8300 or 8400 < wavetime < 8500 or 8600 < wavetime < 8700:
            textt('The first storm is coming', 50, 100, 70)
        elif 8800 < wavetime < 8900 or 9000 < wavetime < 9050 or 9100 < wavetime < 9150 or 9200 < wavetime < 9250 or 9300 < wavetime < 9350 or 9400 < wavetime < 9450:
            screen.fill((0,0,0))
        elif 9500 < wavetime < 9550 or 9600 < wavetime < 9650 or 9700 < wavetime < 9750 or 9800 < wavetime < 9850 or 9900 < wavetime < 9950:
            screen.fill((0,0,0))

        if 4000 < wavetime - 15000 < 4800 or 5600 < wavetime - 15000 < 6400 or 7000 < wavetime - 15000 < 7600 or 8200 < wavetime - 15000 < 8300 or 8400 < wavetime - 15000 < 8500 or 8600 < wavetime - 15000 < 8700:
            textt('The second storm is coming', 50, 100, 70)
        elif 8800 < wavetime - 15000 < 8900 or 9000 < wavetime - 15000 < 9050 or 9100 < wavetime - 15000 < 9150 or 9200 < wavetime - 15000 < 9250 or 9300 < wavetime - 15000 < 9350 or 9400 < wavetime - 15000 < 9450:
            screen.fill((0,0,0))
        elif 9500 < wavetime - 15000 < 9550 or 9600 < wavetime - 15000 < 9650 or 9700 < wavetime - 15000 < 9750 or 9800 < wavetime - 15000 < 9850 or 9900 < wavetime - 15000 < 9950:
            screen.fill((0,0,0))

        if 4000 < wavetime - 30000 < 4800 or 5600 < wavetime - 30000 < 6400 or 7000 < wavetime - 30000 < 7600 or 8200 < wavetime - 30000 < 8300 or 8400 < wavetime - 30000 < 8500 or 8600 < wavetime - 30000 < 8700:
            textt('The infinite storm is coming', 50, 100, 70)
        elif 8800 < wavetime - 30000 < 8900 or 9000 < wavetime - 30000 < 9050 or 9100 < wavetime - 30000 < 9150 or 9200 < wavetime - 30000 < 9250 or 9300 < wavetime - 30000 < 9350 or 9400 < wavetime - 30000 < 9450:
            screen.fill((0,0,0))
        elif 9500 < wavetime - 30000 < 9550 or 9600 < wavetime - 30000 < 9650 or 9700 < wavetime - 30000 < 9750 or 9800 < wavetime - 30000 < 9850 or 9900 < wavetime - 30000 < 9950:
            screen.fill((0,0,0))

        # 피뢰침 리스트에서 피뢰침들 추가
        if len(rodblitlist) != 0:
            for i in rodblitlist:
                screen.blit(lightningrod_img, i)

        # 게임 요소 상태 변경
        # boy 이동/그리기
        global position

        life_location_list = [[40 * (5 - i) + start_life_location, 10] for i in range(lifenumber)]

        boy_pos = [position, 560]

        # 나중에 나오겠지만 아이템이 구동중이지 않을 때는 time_item_item이름 = -1 이고
        # 아이템을 먹으,면 time_item_item이름 이 그 시각 + 5000으로 바뀐다.
        if time_item_umbrella!=-1:
            falling_img=coin_img
            boy_img=boy2_img
            speed_raindrop=5
            speed_item=4
            raindropaddingtime=10
        elif time_item_snowflake!=-1:
            falling_img = snimg
            boy_img=boy1_img
            speed_raindrop=2.5
            speed_item=2
            raindropaddingtime=5
        else:
            falling_img=rdimg
            boy_img=boy1_img
            speed_raindrop=5
            speed_item=4
            raindropaddingtime=10

        # boy1_img가 우산을 안쓴 소년이고 boy2_img가 우산을 쓴 소년인데 두 img 크기가 달라서
        # 바닥의 높이를 맞춰주기 위해서 boy_pos의 y좌표를 img에 따라 다르게 한다.
        if boy_img == boy1_img:
            boy_pos[1] = 560
        else:
            boy_pos[1] = 530

        # 오른쪽키가 눌리면 오른쪽으로 움직이고 왼쪽키가 눌리면 왼쪽으로 움직인다.
        keys = pygame.key.get_pressed()
        position += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * v

        # boy가 화면에서 나가지 않게 한다.
        if position < 0:
            position = 0
        elif position > 600:
            position = 600

        screen.blit(boy_img, boy_pos)
        # boy 사각형
        boy_rect = pygame.Rect(boy_img.get_rect())
        boy_rect.left = boy_pos[0]
        boy_rect.top = boy_pos[1]

        # 점수 증가, 게임속도 증가
        score += 1
        text('score', score, 80, 10)
        if score % 100 == 0:
            vec += 0.13

        # raindrop 추가하기
        if wave==0:
            raindroptimer -= raindropaddingtime
        else:
            raindroptimer -= raindropaddingtime*2
            
        if raindroptimer <= 0:
            raindrop_location.append([random.randint(5, size[1]), 0])
            raindroptimer = random.randint(50, 200)

            # 모든 raindrops 이동
        index = 0
        splashtime = 600
        for raindrop in raindrop_location:
            # raindrops 이동 속도
            raindrop[1] += speed_raindrop * vec
            # raindrop에 닿지 않을 때(바닥에 그냥 떨어질 때)
            if raindrop[1] > 640:
                splash_location_floor.append(raindrop)
                splash_time_floor.append(pygame.time.get_ticks())
                raindrop_location.pop(index)

            # raindrop에 닿을 때(boy하고 닿을 때)
            raindroprect = pygame.Rect(falling_img.get_rect())
            raindroprect.left = raindrop[0]
            raindroprect.top = raindrop[1]
            if falling_img == coin_img:
                if raindroprect.colliderect(boy_rect):
                    coinsound.play()
                    score += 100
                    splash_location.append(raindrop)
                    splash_time.append(pygame.time.get_ticks())
                    raindrop_location.pop(index)

            else:
                if boy_img == boy1_img:
                    if lifenumber == 1:
                        if raindroprect.colliderect(boy_rect):
                            splash_location.append(raindrop)
                            splash_time.append(pygame.time.get_ticks())
                            raindrop_location.pop(index)
                            running = False
                            score_history.append(score)
                            max_score = max(score_history)
                            diesound.play()
                    else:
                        if raindroprect.colliderect(boy_rect):
                            splash_location.append(raindrop)
                            splash_time.append(pygame.time.get_ticks())
                            raindrop_location.pop(index)
                            lifenumber -= 1
                            coldsound.play()
                else:
                    if raindroprect.colliderect(boy_rect):
                        splash_location.append(raindrop)
                        splash_time.append(pygame.time.get_ticks())
                        raindrop_location.pop(index)

                # raindrops 그리기
            screen.blit(falling_img, (raindrop[0], raindrop[1]))
            index += 1

        # 우박
        # 우박 추가하기
        if wave != 0:
            if wave == 1:
                hailtimer -= hailaddingtime
            else:
                hailtimer -= hailaddingtime*2
            if hailtimer <= 0:
                hail_location.append([random.randint(5, size[1]), 0])
                hailtimer = random.randint(50, 200)

            index = 0
            for hail in hail_location:
                # 우박 이동 속도
                hail[1] += speed_hail * vec
                # 우박에 닿지 않을 때(바닥에 그냥 떨어질 때)
                if hail[1] > 640:
                    hail_location.pop(index)

                # 우박에 닿을 때(boy하고 닿을 때)
                hailrect = pygame.Rect(haimg.get_rect())
                hailrect.left = hail[0]
                hailrect.top = hail[1]
                if boy_img == boy1_img:
                    if lifenumber <= 2:
                        if hailrect.colliderect(boy_rect):
                            hail_location.pop(index)
                            running = False
                            score_history.append(score)
                            max_score = max(score_history)
                            diesound.play()
                    else:
                        if hailrect.colliderect(boy_rect):
                            hail_location.pop(index)
                            lifenumber -= 2
                            coldsound.play()
                elif boy_img == boy2_img:
                    if hailrect.colliderect(boy_rect):
                        hail_location.pop(index)                       
                        time_item_umbrella = -1
            
                    # 우박들 그리기
                screen.blit(haimg, (hail[0], hail[1]))
                index += 1

    # splash 그리기를 두 개로 나눈 이유는 splash 그리기 1 코드만 있으면 바닥에서 splash 이미지가 잘린다.

        # splash 그리기 1 - boy랑 닿을 때
        index = 0
        for a in splash_location:
            if falling_img == rdimg:
                if pygame.time.get_ticks() - splash_time[index] < splashtime:
                    screen.blit(splash_img, (a[0], a[1]))
                else:
                    splash_location.pop(index)
                    splash_time.pop(index)
                index += 1

        # splash 그리기 2 - 바닥에 닿을 때
        index = 0
        for a in splash_location_floor:
            if falling_img == rdimg:
                if pygame.time.get_ticks() - splash_time_floor[index] < splashtime:
                    screen.blit(splash_img, (a[0], 620))
                else:
                    splash_location_floor.pop(index)
                    splash_time_floor.pop(index)
                index += 1

        # 우산 아이템
        index2 = 0
        a = random.randint(1, 500)
            # 우산 아이템 생성
        if a == 1:
            item_umbrella_location.append([random.randint(4, 476), 4])
        for umb in item_umbrella_location:
            umb[1] += speed_item + vec
            # 우산 아이템 화면 밖으로 나가면 삭제
            if umb[1] > 640:
                item_umbrella_location.pop(index2)
            umbrect = pygame.Rect(item_umbrella_img.get_rect())
            umbrect.left = umb[0]
            umbrect.top = umb[1]

            # 우산 아이템 boy와 부딪혔을 때 - 우산 아이템 발동
            if umbrect.colliderect(boy_rect):
                time_item_snowflake=-1
                score+=200
                t=5
                time_item_umbrella=pygame.time.get_ticks()+5000
                item_umbrella_location.pop(index2)

            screen.blit(item_umbrella_img, (umb[0], umb[1]))
            index2 += 1

        # 눈 아이템
        index3 = 0
        a = random.randint(1, 500)
        if a == 1:
            item_snowflake_location.append([random.randint(4, 476), 4])
        for snow in item_snowflake_location:
            snow[1] += speed_item + vec
            # 눈 아이템 화면 밖으로 나가면 삭제
            if snow[1] > 640:
                item_snowflake_location.pop(index3)
            snowrect = pygame.Rect(item_snowflake_img.get_rect())
            snowrect.left = snow[0]
            snowrect.top = snow[1]

            # 눈 아이템 boy와 부딪혔을 때 - 눈 아이템 발동
            if snowrect.colliderect(boy_rect):
                time_item_umbrella=-1
                t=5
                time_item_snowflake=pygame.time.get_ticks()+5000
                score+=200
                item_snowflake_location.pop(index3)

            screen.blit(item_snowflake_img, (snow[0], snow[1]))
            index3 += 1

        # 물약 아이템
        index4 = 0
        a = random.randint(1, 500)
        if a == 1:
            item_potion_location.append([random.randint(4, 476), 4])
        for potion in item_potion_location:
            potion[1] += speed_item + vec

            # 물약 아이템 화면 밖으로 나가면 삭제
            if potion[1] > 640:
                item_potion_location.pop(index4)
            potionrect = pygame.Rect(item_potion_img.get_rect())
            potionrect.left = potion[0]
            potionrect.top = potion[1]

            # 물약 아이템 boy와 부딪혔을 때 - 물약 아이템 발동
            if lifenumber < 5:
                if potionrect.colliderect(boy_rect):
                    item_potion_location.pop(index4)
                    score += 200
                    lifenumber += 1
            else:
                if potionrect.colliderect(boy_rect):
                    item_potion_location.pop(index4)
                    score += 200
            screen.blit(item_potion_img, (potion[0], potion[1]))
        
        # 피뢰침 아이템
        index5 = 0
        a = random.randint(1, 400)
            # 피뢰침 아이템 생성
        if a == 1:
            item_lightningrod_location.append([random.randint(4, 476), 4])
        for rod in item_lightningrod_location:
            rod[1] += speed_item + vec
            # 피뢰침 아이템 화면 밖으로 나가면 삭제
            if rod[1] > 640:
                item_lightningrod_location.pop(index5)
            rodrect = pygame.Rect(item_lightningrod_img.get_rect())
            rodrect.left = rod[0]
            rodrect.top = rod[1]

            # 피뢰침 아이템 boy와 부딪혔을 때 - 피뢰핌 아이템 발동
            if rodrect.colliderect(boy_rect):
                score+=200
                item_lightningrod_location.pop(index5)
                rodnumber += 1
            screen.blit(item_lightningrod_img, (rod[0], rod[1]))
            index5 += 1

        # 우산 아이템 지속시간 끝났을 때
        if time_item_umbrella!=-1 and time_item_umbrella < pygame.time.get_ticks():
            time_item_umbrella=-1

        # 눈 아이템 지속시간 끝났을 때
        if time_item_snowflake!=-1 and time_item_snowflake < pygame.time.get_ticks():
            time_item_snowflake=-1

        # 번개 만들기
        # l4 = [0,600]
        if start_thunder_time == -1 and wave >=2:
            if random.randint(1, 100) == 1:
                start_thunder_time = pygame.time.get_ticks()
                x1=random.randint(5, size[1]-5)
                if 640-x1<60:
                    direction=-1
                elif x1<60:
                    direction=1
                else:
                    direction = random.choice([-1, 1])
                x2=random.choice(range(x1+30*direction, x1+130*direction,direction))
                x3=random.choice(range(x2-30*direction, x2-130*direction, -direction))
                x4=random.choice(range(x3+30*direction, x3+130*direction, direction))
                l1 = [x1, 0]
                l2 = [x2, 200]
                l3 = [x3, 400]
                l4 = [x4, 600]
                if len(rodblitlist) != 0:
                    l4[0] = rodblitlist[0][0]
                l=l1[:]
                location=[l1]
        # 여기서 try except를 하는 이유는 번개가 아직 한 번도 치지 않았는데 우산 아이템 먹는 경우 l4가 없어서 오류가 나기 때문이다
        try:
            if len(rodblitlist) == 0:
                if time_item_umbrella != -1:
                    l4[0] = boy_pos[0]
        except UnboundLocalError:
            pass
        if start_thunder_time != -1:
            for _ in range(10):
                if len(location) <= 150:
                    l[0] += (l2[0]-l1[0])/150
                    l[1] += (l2[1]-l1[1])/150
                elif 100 < len(location) <= 300:
                    l[0] += (l3[0]-l2[0])/150
                    l[1] += (l3[1]-l2[1])/150
                elif 200 < len(location) <= 450:
                    l[0] += (l4[0]-l3[0])/150
                    l[1] += (l4[1]-l3[1])/150
                location.append(l[:])
            index=0
            for thu in location:
                thurect = pygame.Rect(thunder_img.get_rect())
                thurect.left = thu[0]
                thurect.top = thu[1]
                if thurect.colliderect(boy_rect):
                    running = False
                    score_history.append(score)
                    max_score = max(score_history)
                    diesound.play()
            index += 1

            for i in location:
                screen.blit(thunder_img, i)

        # 번개가 피뢰침 맞으면 피뢰침 없애기
        if len(rodblitlist) != 0:
            try:
                if len(location) >= 450 and spacetime[0] < start_thunder_time: # 번개가 나오기 시작한 후 피뢰침을 깔면 다음 번개에서 발동
                    rodblitlist.pop(0)
                    spacetime.pop(0)
                    start_thunder_time = -1
                    location = []
            except UnboundLocalError:
                pass
        # 피뢰침 없을 때
        try:
            if len(location) >= 450:
                start_thunder_time = -1
                location=[]
        except UnboundLocalError:
            pass       

        # 아이템 지속시간 표시
        try:
            if time_item_umbrella != -1:
                timer(round(t, 2), item_umbrella_img)
            elif time_item_snowflake != -1:
                timer(round(t, 2), item_snowflake_img)
            t -= 1/50
        except UnboundLocalError:
            pass

        # 설치 가능한 피뢰침 개수 표시
        screen.blit(item_lightningrod_img, (550, 45))
        textt(rodnumber, 24, 600, 55)

        # 생명 하트 띄우기
        for i in life_location_list:
            screen.blit(life_img, i)
        
        # 게임 속도
        fpsClock.tick(FPS)

        # 화면 전체 업데이트
        pygame.display.flip()
    endsc(score)

def endsc(score):
    # 게임 종료 화면
    screen.blit(gameover, (0, 0))
    text('score', score, screen.get_rect().centerx, screen.get_rect().centery - 100)
    text('best score', max_score, screen.get_rect().centerx, screen.get_rect().centery + 30 - 100)
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gamestart()
gamestart()
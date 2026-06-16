import pygame
import sys
import random
import time
from pathlib import Path

base_path = Path(__file__).resolve().parent

file_path = base_path / "./data/PB.txt"

with open(file_path, "r", encoding="utf-8") as f:
    content_str = f.read()

content = int(content_str)


#game config
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

pygame.init()

HP = int(10)
muteki = int(0)
dameg_tilt = int(0)
timer = int(0)
sec = int(0)
start =  int(3)
font = pygame.font.SysFont(None, 36)
font_big = pygame.font.SysFont(None, 256)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("yokeru")

clock = pygame.time.Clock()

#プレイヤーconfig
player_width = 50
player_height = 50

player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height - 20
player_speed = 10

#障害物　辞書型
obstacles = []

for i in range(5):
    obs = {
        "x": random.randint(0,800),
        "y": random.randint(-300,-30),
        "size": random.choice([100,125]),
        "speed":random.choice([7,12]),
    }
    obstacles.append(obs)

for i in range(4):

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    start_text = str(start)
    start_image = font_big.render(start_text, True, (255, 255, 255))
    x_pos = (SCREEN_WIDTH // 2) - (start_image.get_width() // 2)
    y_pos = (SCREEN_HEIGHT // 2) - (start_image.get_height() // 2)
    screen.blit(start_image, (x_pos, y_pos))

    pygame.display.update()

    start -= 1
    time.sleep(1)



#maim loop
while True:

    timer += 1
    if timer == 60:
        timer = 0
        sec += 1


    clock.tick(60)

    screen.fill((0,0,0))

    if muteki > 0:
        muteki -= 1

    if dameg_tilt > 0:
        dameg_tilt-= 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  
        player_x -= player_speed
    if keys[pygame.K_RIGHT]: 
        player_x += player_speed
    
    #プレイヤーを画面内に
    if player_x < 0:
        player_x = 0
    if player_x > SCREEN_WIDTH - player_width:
        player_x = SCREEN_WIDTH - player_width


    #障害物
    for obs in obstacles:
        obs["y"] += obs["speed"]

        #ダメージ処理
        if (player_x < obs["x"] + obs["size"] and player_x + player_width > obs["x"]) and \
           (player_y < obs["y"] + obs["size"] and player_y + player_height > obs["y"]):
            
            if muteki == 0:
                HP -= 1
                muteki += 30
                dameg_tilt += 30
        
        #障害物の再生成
        if obs["y"] > 600:
            obs["y"]= -50
            obs["size"] = random.choice([100,125])
            obs["x"]= random.randint(0,800)
            obs["speed"] = random.randint(7,12)

        pygame.draw.rect(screen, (255, 255, 0), (obs["x"], obs["y"], obs["size"], obs["size"]))

    #見た目の処理
    if muteki <= 0:
        pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_width, player_height))

    elif dameg_tilt <= 0:
        pygame.draw.rect(screen, (0, 128, 0), (player_x, player_y, player_width, player_height))
    else:
        pygame.draw.rect(screen, (255, 0,0), (player_x, player_y, player_width, player_height))

    hp_text = f"HP: {HP}"
    hp_image = font.render(hp_text, True, (255, 255, 255))
    screen.blit(hp_image, (20, 20))

    minutes, seconds = divmod(sec, 60)
    time_text = f"{minutes}:{seconds:02d}"
    time_img = font.render(time_text, True, (255,255,255))
    screen.blit(time_img,(20,50))

    #終了処理
    if HP <= 0:
        print(f"記録:{minutes:02d}:{seconds:02d}")

        if sec >= content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(sec))

                minutes_pb, seconds_pb = divmod(content, 60)
                pb_time_text = f"{minutes_pb}:{seconds_pb:02d}"

                print("PB更新!")
                print(f"前回までのPB:{pb_time_text}")
        else:
            minutes_pb, seconds_pb = divmod(content, 60)
            print(f"現在のPB: {minutes_pb:02d}:{seconds_pb:02d}")

        pygame.quit()
        sys.exit()
        

    pygame.display.update()


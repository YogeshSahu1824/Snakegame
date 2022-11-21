from opcode import opname
from tkinter.font import BOLD, ITALIC
import pygame
import random
import os

pygame.mixer.init()
pygame.init()
# backgroud Imagge


# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
neavy_blue = (32, 42, 68)
grey = (220, 220, 220)
# Creating Windows
screen_width = 700
screen_height = 600


Gamewindow = pygame.display.set_mode((screen_width, screen_height))
bgimg=pygame.image.load("bgimage.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height))
pygame.display.set_caption("ITS MY FIRST GAME")
# pygame.time.Clock() take the value how many frame show in a sigle second so it take fps
pygame.display.update()
clock = pygame.time.Clock()
# pygame.font.init()
font = pygame.font.SysFont(None, 50)



def text_screen(text, color, x, y):
    # font.render()
    screen_text = font.render(text, True, color)
    Gamewindow.blit(screen_text, [x, y])

# Gamewindow.fill(red)


def plot_snake(Gamewindow, color, snake_list, snake_size, snake_size1):
    for x, y in snake_list:
        pygame.draw.rect(Gamewindow, color, [x, y, snake_size, snake_size1])
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)
def WelcomeScreen():
    game_exit=False
    while not game_exit:
        Gamewindow.fill((233,210,229))
        text_screen("Welcome To Snake Game",black,110,200)
        text_screen("Press Spacebar to Play  the Game",black,55,250)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        pygame.mixer.music.load("backgroundmusic.mp3")
                        pygame.mixer.music.play()
                        Gameloop()
        pygame.display.update()
        clock.tick(60)
def Gameloop():
    game_exit = False
    game_over = False
    # coordinates
    snake_x = 45
    snake_y = 55
    # Size of the Sanke
    snake_size = 20
    snake_size1 = 20
    # Velocity of the Sanke
    velocity_x = 0
    velocity_y = 0
    init_velocity = 4
    fps = 30
    snake_list = []
    snake_lenght = 1
    score = 0
    food_x = random.randint(20, screen_width-50)
    food_y = random.randint(20, screen_height-50)
    # fps is used to show the image in a screen in single second
    #  60 fps means 60 frame per second
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt",'r') as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        highscore=f.read()
    while not game_exit:
        if game_over:
            with open("highscore.txt",'w') as f:
                f.write(str(highscore))
            Gamewindow.fill(white)
            text_screen("Game Over ! To Conitnue Press Enter ", red, 50, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("backgroundmusic.mp3")
                        pygame.mixer.music.play()
                        Gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key==pygame.K_q:
                        score+=10
                if event.type == MUSIC_END:
                         print('music end event')
                         pygame.mixer.music.load("backgroundmusic.mp3")
                         pygame.mixer.music.play()
                         
            snake_x = snake_x+velocity_x
            snake_y = snake_y+velocity_y
            if abs(snake_x-food_x) < 20 and abs(snake_y-food_y) < 20:
                score += 10
                food_x = random.randint(20, screen_width-50)
                food_y = random.randint(20, screen_height-50)
                snake_lenght += 5
                if score>int(highscore):
                    highscore=score
            Gamewindow.fill(white)
            Gamewindow.blit(bgimg,(0,0))
        # text_screen=("SCORE:"+str(score*10),red,5,5)
            text_screen("Score: " + str(score)+" Highscore:"+str(highscore), black, 10, 10)
            pygame.draw.rect(Gamewindow, red, [food_x, food_y, snake_size, snake_size1])
            head = []
            head.append(snake_x)
            head.append(snake_y)
    
            snake_list.append(head)
            if head in snake_list[:-2]:
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                game_over=True
            if snake_x<0 or snake_y<0 or snake_x > screen_width or snake_y > screen_height:
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                game_over=True
    
            if len(snake_list) > snake_lenght:
                del snake_list[0]
            plot_snake(Gamewindow, black, snake_list, snake_size, snake_size1)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
# Gameloop()
WelcomeScreen()

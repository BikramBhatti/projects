import pygame
import os
import random

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (20, 20)

from pygame import *

init()
size = width, height = 1000, 700
screen = display.set_mode(size)


# load images
stop_img = pygame.image.load("stop.png")
stop_img = pygame.transform.scale(stop_img, (30, 30))

cross_img = pygame.image.load("cross.jpg")
cross_img = pygame.transform.scale(cross_img, (30, 30))

####################################
# define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARKGREEN = (19, 156, 32)
PURPLE = (145, 23, 232)
YELLOW = (225, 232, 23)
DARKBLUE = (13, 9, 107)

boxX = 100
box1Y = 100
box2Y = 250
box3Y = 400
boxW = 400
boxH = 100
r1x = random.randint(35, 965)
r1y = random.randint(100, 600)
r2x = random.randint(35, 965)
r2y = random.randint(100, 600)
r3x = random.randint(35, 965)
r3y = random.randint(100, 600)
r4x = random.randint(35, 965)
r4y = random.randint(100, 600)

rect11 = Rect(r1x, r1y, 50, 50)
rect22 = Rect(r2x, r2y, 50, 50)
rect33 = Rect(r3x, r3y, 50, 50)
rect44 = Rect(r4x, r4y, 50, 50)

sp1 = random.randint(2, 5)
sp2 = random.randint(6, 9)
sp3 = random.randint(2, 5)
sp4 = random.randint(6, 9)
sp5 = random.randint(2, 5)
sp6 = random.randint(6, 9)
sp7 = random.randint(2, 5)
sp8 = random.randint(6, 9)

red_x = random.randint(0, width - 50)
red_y = 75
red_speed = 5

red_2x = random.randint(0, width - 50)
red_2y = 75
red2_speed = 5

score = 0

word0 = "Catch the Fruit"
word1 = "PLAY"
word2 = "LEVELS"
word3 = "INSTRUCTIONS"
#word4 = "Points :"+str(score)
word5 = "Level : "


def drawText(screen, message, font, color, x, y):
    text = font.render(message, True, color)
    screen.blit(text, (x, y))


titleFont = font.SysFont("Times New Roman", 60)
menuFont = font.SysFont("Times New Roman", 40)

titleText = titleFont.render(word0, True, BLACK)

text1 = menuFont.render(word1, 1, RED)
text2 = menuFont.render(word2, 1, RED)
text3 = menuFont.render(word3, 1, RED)
#text4 = menuFont.render(word4, 1, RED)
text5 = menuFont.render(word5, 1, RED)

text1W, text1H = menuFont.size(word1)
text1X = boxX + (boxW - text1W) // 2
text1Y = box1Y + (boxH - text1H) // 2

text2W, text2H = menuFont.size(word2)
text2X = boxX + (boxW - text2W) // 2
text2Y = box2Y + (boxH - text2H) // 2

text3W, text3H = menuFont.size(word3)
text3X = boxX + (boxW - text3W) // 2
text3Y = box3Y + (boxH - text3H) // 2

STATE_MENU = 0
STATE_GAME = 1
STATE_LEVELS = 2
STATE_INSTRUCTIONS = 3


def drawMenu(screen, button, mx, my, state):
    screen.fill(DARKGREEN)

    titleX = width // 2 - titleText.get_width() // 2
    titleY = 30
    screen.blit(titleText, (titleX, titleY))

    rect1 = Rect(boxX, box1Y, boxW, boxH)
    rect2 = Rect(boxX, box2Y, boxW, boxH)
    rect3 = Rect(boxX, box3Y, boxW, boxH)

    draw.rect(screen, GREEN, rect1)
    draw.rect(screen, GREEN, rect2)
    draw.rect(screen, GREEN, rect3)

    screen.blit(text1, (text1X, text1Y, text1W, text1H))
    screen.blit(text2, (text2X, text2Y, text2W, text2H))
    screen.blit(text3, (text3X, text3Y, text3W, text3H))

    if rect1.collidepoint(mx, my):
        draw.rect(screen, BLACK, rect1, 5)
        if button == 1:
            state = STATE_GAME
    elif rect2.collidepoint(mx, my):
        draw.rect(screen, BLACK, rect2, 5)
        if button == 1:
            state = STATE_LEVELS
    elif rect3.collidepoint(mx, my):
        draw.rect(screen, BLACK, rect3, 5)
        if button == 1:
            state = STATE_INSTRUCTIONS

    return state


def drawGame(screen, button, mx, my, state, score):
    draw.rect(screen, WHITE, (0, 0, width, height))
    pygame.draw.line(screen, BLACK, (0, 75), (1000, 75), 5)
    word4 = "Points :" + str(score)
    text4 = menuFont.render(word4, 1, BLACK)
    text5 = menuFont.render(word5, 1, BLACK)
    screen.blit(text4, (30, 20))
    screen.blit(text5, (700, 20))

    rect11 = Rect(r1x, r1y, 50, 50)
    rect22 = Rect(r2x, r2y, 50, 50)
    rect33 = Rect(r3x, r3y, 50, 50)
    rect44 = Rect(r4x, r4y, 50, 50)


    # pygame.draw.rect(screen, YELLOW, rect11)
    # pygame.draw.rect(screen, YELLOW, rect22)
    # pygame.draw.rect(screen, YELLOW, rect33)
    # pygame.draw.rect(screen, YELLOW, rect44)
    screen.blit(cross_img,rect11)
    screen.blit(cross_img, rect22)
    screen.blit(cross_img, rect33)
    screen.blit(cross_img, rect44)

    # pygame.draw.rect(screen, RED, (red_x, red_y, 50, 50))
    # pygame.draw.rect(screen, RED, (red_2x, red_2y, 50, 50))
    screen.blit(stop_img,pygame.draw.rect(screen, RED, (red_x, red_y, 50, 50)))
    screen.blit(stop_img, pygame.draw.rect(screen, RED, (red_2x, red_2y, 50, 50)))
    if button == 1:
        if rect11.collidepoint(mx,my):
            score = score+1
        elif rect22.collidepoint(mx,my):
            score = score+1
        elif rect33.collidepoint(mx,my):
            score = score+1
        elif rect44.collidepoint(mx,my):
            score = score+1


    if button == 3:
        state = STATE_MENU
    return state, score


def drawLevels(screen, button, mx, my, state):
    draw.rect(screen, BLUE, (0, 0, width, height))
    if button == 3:
        state = STATE_MENU
    return state


def drawInstructions(screen, button, mx, my, state):
    draw.rect(screen, GREEN, (0, 0, width, height))
    drawText(screen, "1 ) Catch the fruits to earn points.", menuFont, BLACK, 50, 60)
    drawText(screen, "2) Avoid the bombs or you lose a life!", menuFont, BLACK, 50, 100)
    drawText(screen, "3) Use LEFT and RIGHT arrow keys to move.", menuFont, BLACK, 50, 140)
    drawText(screen, "4) The game gets harder over time.", menuFont, BLACK, 50, 180)
    drawText(screen, "(Right-click to go back)", menuFont, BLACK, 500, 600)
    if button == 3:
        state = STATE_MENU
    return state


running = True
myClock = time.Clock()

state = STATE_MENU
mx = my = 0

while running:
    button = 0
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mx, my = e.pos
            button = e.button
        if e.type == MOUSEMOTION:
            mx, my = e.pos

    if state == STATE_MENU:
        state = drawMenu(screen, button, mx, my, state)
    elif state == STATE_GAME:
        state, score = drawGame(screen, button, mx, my, state,score)

        red_y += red_speed
        if red_y > height:
            red_y = 75
            red_x = random.randint(0, width - 50)



    elif state == STATE_LEVELS:
        state = drawLevels(screen, button, mx, my, state)
    elif state == STATE_INSTRUCTIONS:
        state = drawInstructions(screen, button, mx, my, state)
    else:
        running = False

    # Yellow box movement
    r1x += sp1
    r1y += sp2
    if r1x + 35 > 1000 or r1x - 35 < 0:
        sp1 *= -1
    if r1y - 35 < 75 or r1y + 35 > 700:
        sp2 *= -1

    r2x += sp3
    r2y += sp4
    if r2x + 35 > 1000 or r2x - 35 < 0:
        sp3 *= -1
    if r2y - 35 < 75 or r2y + 35 > 700:
        sp4 *= -1

    r3x += sp5
    r3y += sp6
    if r3x + 35 > 1000 or r3x - 35 < 0:
        sp5 *= -1
    if r3y - 35 < 75 or r3y + 35 > 700:
        sp6 *= -1

    r4x += sp7
    r4y += sp8
    if r4x + 35 > 1000 or r4x - 35 < 0:
        sp7 *= -1
    if r4y - 35 < 75 or r4y + 35 > 700:
        sp8 *= -1

    red_2y += red_speed
    if red_2y > height:
        red_2y = 75
        red_2x = random.randint(0, width - 50)

    display.flip()
    myClock.tick(60)

quit()

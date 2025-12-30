import pygame
from pygame import event

# Initialize Pygame
pygame.init()

# window size
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Assignment")


# create house
def draw_house(screen1):
    screen1.fill("WHITE")

# create  the roof
    roof = [(200, 250), (400, 150), (600, 250)]
    pygame.draw.polygon(screen1, "BROWN", roof)
    pygame.draw.polygon(screen1, "BLACK", roof, 3)

# create the house rectangle
    house_rect = pygame.Rect(250, 250, 300, 250)
    pygame.draw.rect(screen1,"RED", house_rect)
    pygame.draw.rect(screen1, "BLACK", house_rect, 3)

# create the circular window
    pygame.draw.circle(screen1, "WHITE", (400, 210), 30)
    pygame.draw.circle(screen1, "BLACK", (400, 210), 30, 3)

# create chimney
    chimney_rect = pygame.Rect(500, 180, 20, 70)
    pygame.draw.rect(screen1, "BROWN", chimney_rect)
    pygame.draw.rect(screen1, "BLACK", chimney_rect, 3)

# create door
    door_rect = pygame.Rect(280, 350, 70, 150)
    pygame.draw.rect(screen1, "GREY", door_rect)
    pygame.draw.rect(screen1, "BLACK", door_rect, 3)

# create inner rectangle

    door_rect1 = pygame.Rect(290, 370, 50, 50)
    pygame.draw.rect(screen1, "WHITE", door_rect1)
    pygame.draw.rect(screen1, "BLACK", door_rect1, 3)

# create door knob
    pygame.draw.circle(screen1, "BLACK", (345, 425), 5)

# create Window
    window_rect = pygame.Rect(380, 300, 140, 100)
    pygame.draw.rect(screen1, "WHITE", window_rect)
    pygame.draw.rect(screen1, "BLACK", window_rect, 3)

# create windows pane
    pygame.draw.line(screen1, "BLACK", (450, 300), (450, 400), 3)
    pygame.draw.line(screen1, "BLACK", (380, 350), (520, 350), 3)

# create  trees
    pygame.draw.rect(screen1, "WHITE", (190, 320, 20, 80))
    pygame.draw.rect(screen1, "BLACK", (190, 320, 20, 80), 3)
    pygame.draw.circle(screen1, "GREEN", (200, 300), 30)
    pygame.draw.circle(screen1, "BLACK", (200, 300), 30, 3)

    pygame.draw.rect(screen1, "WHITE", (590, 320, 20, 80))
    pygame.draw.rect(screen1, "BLACK", (590, 320, 20, 80), 3)
    pygame.draw.circle(screen1, "GREEN", (600, 300), 30)
    pygame.draw.circle(screen1, "BLACK", (600, 300), 30, 3)


# create clouds
    pygame.draw.circle(screen1, "BLUE", (150, 100), 30)
    pygame.draw.circle(screen1, "BLUE", (180, 90), 40)
    pygame.draw.circle(screen1, "BLUE", (210, 100), 30)

    pygame.draw.circle(screen1, "BLUE", (500, 80), 30)
    pygame.draw.circle(screen1, "BLUE", (530, 70), 40)
    pygame.draw.circle(screen1, "BLUE", (560, 80), 30)


game_running = True
while game_running:
    draw_house(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

import pygame
import time
import random


pygame.init()
display_width = 800
display_height = 600
car_width = 73
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
block_color = (53, 115, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car")
clock = pygame.time.Clock()
carImg = pygame.image.load("Car.png").convert()

def things_dodged(count1, count2):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count1)+" Level: "+ str(count2), True, black)
    gameDisplay.blit(text, (0, 0))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay,block_color,[thingx ,thingy, thingw, thingh])


def crash():
    message_display('You Crashed')


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    dodged = 0
    level = 1
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged, level)
        if x > display_width - car_width or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged +=1
            if dodged % 20 == 0:
                level +=1
            thing_speed +=level*0.3
            thing_width +=random.randrange(-50,50)
        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
               crash()
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
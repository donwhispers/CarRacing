import pygame
import time
import random


pygame.init()
display_width = 400
display_height = 650
car_width = 44
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
block_color = (53, 115, 255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car")
clock = pygame.time.Clock()
carImg = pygame.image.load("Car.png").convert()
car2Img = pygame.image.load("Car2.png").convert()
bg = pygame.image.load("road.png").convert()
pygame.mixer.music.load('sound.ogg')


def things_dodged(count1, count2, score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count1)+" Level: " + str(count2), True, white)
    gameDisplay.blit(text, (0, 0))
    text1 = font.render("Best score: " + score, True, white)
    gameDisplay.blit(text1, (0, 30))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def things(thingx, thingy):
    gameDisplay.blit(car2Img, (thingx, thingy))


def writerecord(count, score):
    if score < count:
        f = open('best_score.txt', 'w')
        f.write(str(count))
        f.close()


def crash():
    message_display('You Crashed')


def game_loop():
    pygame.mixer.music.play()
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    f = open('best_score.txt', 'r')
    bscore = f.read()
    f.close()
    thing_startx = random.randrange(0, display_width)
    thing_starty = -200
    thing_speed = 4
    dodged = 0
    level = 1
    bscore.split()
    gameExit = False
    while not gameExit:
        gameDisplay.blit(bg, (0, 0))
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
        things(thing_startx, thing_starty)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged, level, bscore)
        if thing_starty > display_height:
            thing_starty = 0 - 139
            thing_startx = random.randrange(0,342)
            dodged +=1
            if dodged % 20 == 0:
                prom = random.randrange(1, 3)
                level +=1
                thing_speed = thing_speed + prom + level
        if x > display_width - car_width or x < 0:
            writerecord(dodged, (int(bscore)))
            crash()
        if y < thing_starty + 139:
            if x > thing_startx and x < thing_startx + 58 or x + car_width > thing_startx and x + car_width < thing_startx + 58:
                writerecord(dodged, int(bscore))
                crash()
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()

import pygame
import sys
import random

pygame.init()
width = 1200
height = 800

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake')

green = 0,255,0
RED = 255,0,255
BLACK = 0,0,0
white = 255,255,255

clock = pygame.time.Clock()

block_size = 15
fps = 60

font = pygame.font.SysFont(None, 25)

def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

# rectangle: [x, y, w, h]
def rect_overlap(a, b):
    return \
    a[0] < b[0] + b[2] and \
    a[0] + a[2] > b[0] and \
    a[1] < b[1] + b[3] and \
    a[1] + a[3] > b[1]    

    
def message_to_screen(msg, colour):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [width/2,height/2])

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = width/2
    lead_y = height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, width-block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0, height-block_size))#/10.0)*10.0
    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(BLACK)
            message_to_screen("Game over, press C to play again or Q to quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            gameOver = True
      

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(BLACK)

        AppleThickness = 30
        pygame.draw.rect(gameDisplay, RED, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        
        snake(block_size, snakeList)

        
        pygame.display.update()

        if rect_overlap((lead_x, lead_y, block_size, block_size), (randAppleX, randAppleY, AppleThickness, AppleThickness)):
                randAppleX = round(random.randrange(0, width-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0, height-block_size))#/10.0)*10.0
                snakeLength += 1            
         
        clock.tick(fps)
        
    pygame.quit()
    quit()

gameLoop()
pygame.quit()

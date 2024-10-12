
import pygame
from pygame.locals import *
import sys
import random


#2- Define Constants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

#3-Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4.Load the images, sounds etc.
ballImage = pygame.image.load('C:\\Users\\18073\\Desktop\\Data Analyst\\Pygame_practice\\pygame_demo_image\\ball.png')


#5. Initialize Variables
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)

#Image transformation
new_ball_Image = pygame.transform.scale(ballImage,(ballX, ballY)) 

xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

#6.Loop forever
while True:
    #7. check for Handling events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit()

    #8.Do any frame Works
    if (ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = - xSpeed    #reverse x direction

    if (ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed
    
    #update the bvall location, using the speed in two directions
    ballX = ballX + xSpeed
    ballY = ballY + ySpeed

    #9.clear the window before drawing it again
    window.fill(BLACK)

    #10. draw the window elements
    window.blit(new_ball_Image, (ballX, ballY))

    #11. Update the window
    pygame.display.update()

    #12. Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
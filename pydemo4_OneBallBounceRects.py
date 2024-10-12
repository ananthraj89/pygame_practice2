import pygame
from pygame.locals import *
import sys
import random

# 2- Define Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

# 3- Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4- Load the images, sounds, etc.
ballImage = pygame.image.load('C:\\Users\\18073\\Desktop\\Data Analyst\\Pygame_practice\\pygame_demo_image\\ball.png')

# Image transformation (scaling the image to the fixed size of BALL_WIDTH_HEIGHT)
new_ball_Image = pygame.transform.scale(ballImage, (BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT))

# Get the rectangle of the scaled ball image
ballRect = new_ball_Image.get_rect()

# 5- Ensure the ball fits in the window
MAX_WIDTH = max(WINDOW_WIDTH - ballRect.width, 0)
MAX_HEIGHT = max(WINDOW_HEIGHT - ballRect.height, 0)

# Randomize initial position, ensuring it stays within the valid range
ballRect.left = random.randrange(MAX_WIDTH) if MAX_WIDTH > 0 else 0
ballRect.top = random.randrange(MAX_HEIGHT) if MAX_HEIGHT > 0 else 0

xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6. Loop Forever
while True:
    # 7. Check for handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8. Do any per-frame actions
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed  # Reverse X direction

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # Reverse Y direction

    # Update the ball's rectangle using the speed in two directions
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    # 9. Clear the window before drawing it again
    window.fill(BLACK)

    # 10. Draw the window elements
    window.blit(new_ball_Image, ballRect)

    # 11. Update the window
    pygame.display.update()

    # 12. Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)

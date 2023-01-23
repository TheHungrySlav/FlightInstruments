# Simple pygame program

# Import and initialize the pygame library
import math
import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
FPS = 60

# Set up the drawing window
screen = pygame.display.set_mode([700, 700])
black = (0,0,0)
white = (255,255,255)

# Run until the user asks to quit
running = True
# Fill the background with white
screen.fill(white)
pygame.display.flip()

base = pygame.image.load("base.png").convert()
tenthousandft_point = pygame.image.load("10000ft.png").convert()
thousandft_point = pygame.image.load("1000ft.png").convert()
hundredft_point = pygame.image.load("100ft.png").convert()

# Draw the altimeter base
screen.blit(pygame.transform.scale(base, (700, 700)), (0, 0))

# Draw Altimeter pointers
current_altitude = 0

def altitude(current_altitude,direction):
    if direction == 1:
        new_altitude = current_altitude + 10
    if direction == -1:
        new_altitude = current_altitude - 10
        if current_altitude <= 0:
            new_altitude = 0
    if direction == 0:
        new_altitude = current_altitude
    return new_altitude 


def altimeter(current_altitude):

    angle1 = -90 + (3.6*(current_altitude/10))
    angle2 = -90 + (3.6*current_altitude/100)
    angle3 = -90 + (3.6*current_altitude/1000)

    # 10000ft pointer
    tenthouft_point = (360,340)
    len1 = 200
    x_1 = tenthouft_point[0] + math.cos(math.radians(angle1)) * len1
    y_1 = tenthouft_point[1] + math.sin(math.radians(angle1)) * len1

    # 1000ft Pointer
    thouft_point = (360,340)
    len2 = 100
    x_2 = tenthouft_point[0] + math.cos(math.radians(angle2)) * len2
    y_2 = tenthouft_point[1] + math.sin(math.radians(angle2)) * len2

    # 100ft pointer
    hundredft_point = (360,340)
    len3= 160
    x_3 = tenthouft_point[0] + math.cos(math.radians(angle3)) * len3
    y_3 = tenthouft_point[1] + math.sin(math.radians(angle3)) * len3

    # Draw pointers
    pygame.draw.line(screen, Color("white"), tenthouft_point, (x_1,y_1), 1)
    pygame.draw.line(screen, Color("green"), thouft_point, (x_2,y_2), 1)
    pygame.draw.line(screen, Color("red"), hundredft_point, (x_3,y_3), 1)
    pygame.display.update()
    pygame.display.set_caption("Altimeter")


# Define starting speed
while running:
    current_altitude = altitude(current_altitude,0)
    altimeter(current_altitude)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    keys = pygame.key.get_pressed()         
    if keys[pygame.K_UP]:
        #print("Altitude Increasing")
        direction = 1
        screen.blit(pygame.transform.scale(base, (700, 700)), (0, 0))
        current_altitude = altitude(current_altitude,direction)
        altimeter(current_altitude)
    if keys[pygame.K_DOWN]:
        #print("Altitude Decreasing")
        direction = -1
        current_altitude = altitude(current_altitude,direction)
        altimeter(current_altitude)    
    else:
        direction = 0
        current_altitude = altitude(current_altitude,direction)    
        altimeter(current_altitude) 
    screen.fill((0, 0, 0))
    screen.blit(pygame.transform.scale(base, (700, 700)), (0, 0))         
    print(current_altitude)
    clock.tick(FPS)
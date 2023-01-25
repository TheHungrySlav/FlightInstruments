# Simple pygame program

# Import and initialize the pygame library
import math
import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
FPS = 100

# Set up the drawing window
screen = pygame.display.set_mode([1500, 700])
black = (0,0,0)
white = (255,255,255)

# Run until the user asks to quit
running = True
# Fill the background with white
screen.fill(white)
pygame.display.flip()

# Import all pictures
base = pygame.image.load("base.png").convert()
airspeed_base = pygame.image.load("Airspeedgraphic.png").convert()
# Draw the altimeter base
screen.blit(pygame.transform.scale(base, (700, 700)), (0, 0))
# Draw air speed indicator base
screen.blit(pygame.transform.scale(airspeed_base, (700,700)),(750,0))
pygame.display.update()

# Origin Positions
current_altitude = 0
current_airspeed = 0
new_airspeed = 0
acceleration = 0
throttle = 0
direction = 0
angle_of_att = 15

# Calculate airspeed
def airspeed(current_airspeed,throttle):
    if throttle == 1:
        new_airspeed = current_airspeed + 1
        if new_airspeed >=180:
            new_airspeed = 180
            print("Red Line!!!")
    if throttle == -1:
        new_airspeed = current_airspeed - 1
        if new_airspeed < 0:
            new_airspeed = 0
            print("Stalling!")
    elif throttle == 0:
        new_airspeed = current_airspeed
    acceleration = (new_airspeed - current_airspeed)/2    
    return new_airspeed, acceleration

# Calculate Altitude
def altitude(current_altitude,direction,airspeed,acceleration):
    altitude_change = airspeed*math.cos(math.radians(angle_of_att))
    if direction == 1:
        new_altitude = current_altitude + altitude_change
    if direction == -1:
        new_altitude = current_altitude - altitude_change
        if current_altitude <= 0:
            new_altitude = 0
    if direction == 0:
        new_altitude = current_altitude
    return new_altitude 

# Draw Altimeter pointers
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
    pygame.display.set_caption("Instruments")

# Draw Airspeed Indicator
def airspeed_indicator(new_airspeed):
    speed_point = (1110,340)
    len = 200
    angle = -90 + 1.8*(new_airspeed)
    x = speed_point[0] + math.cos(math.radians(angle)) * len
    y = speed_point[1] + math.sin(math.radians(angle)) * len
    pygame.draw.line(screen, Color("white"), speed_point, (x,y), 1)
    pygame.display.update()

# Main Loop
while running:
    new_airspeed, acceleration = airspeed(current_airspeed,throttle)
    airspeed_indicator(new_airspeed)
    current_altitude = altitude(current_altitude,direction,new_airspeed,acceleration)
    altimeter(current_altitude)
    current_airspeed = new_airspeed
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        throttle = 1
        print("Airspeed increasing")
        new_airspeed, acceleration = airspeed(current_airspeed,throttle)
        airspeed_indicator(new_airspeed)
        current_airspeed = new_airspeed
    if keys[pygame.K_s]:
        throttle = -1
        print("Airspeed decreasing")
        new_airspeed, acceleration = airspeed(current_airspeed,throttle)
        airspeed_indicator(new_airspeed)
        current_airspeed = new_airspeed       
    if keys[pygame.K_UP]:
        direction = 1
        # screen.blit(pygame.transform.scale(base, (700, 700)), (0, 0))
        current_altitude = altitude(current_altitude,direction,current_airspeed, acceleration)
        altimeter(current_altitude)
    if keys[pygame.K_DOWN]:
        direction = -1
        current_altitude = altitude(current_altitude,direction,current_airspeed, acceleration)
        altimeter(current_altitude)    
    else:
        direction = 0
        throttle = 0
        new_airspeed, acceleration = airspeed(current_airspeed,throttle)
        airspeed_indicator(new_airspeed)
        current_altitude = altitude(current_altitude,direction,new_airspeed,acceleration)
        altimeter(current_altitude)
        current_airspeed = new_airspeed
    screen.fill((0, 0, 0))
    screen.blit(pygame.transform.scale(base, (700, 700)), (0, 0)) 
    screen.blit(pygame.transform.scale(airspeed_base, (700,700)),(750,0))        
    #print(current_altitude)
    clock.tick(FPS)
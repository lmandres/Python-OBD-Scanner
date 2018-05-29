#!/usr/bin/python

# Import a library of functions called 'pygame'
import pygame
from math import pi, cos, sin

import PyOBD2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

screen = None
font = None
radius = None

def draw_gauge(row, column, value_pct_in, text_1_in, text_2_in):

    value_pct = value_pct_in
    if value_pct <= 0.0:
        value_pct = 0.0
    elif 100.0 <= value_pct:
        value_pct = 100.0

    text1 = font.render(text_1_in, False, WHITE) 
    text2 = font.render(text_2_in, False, WHITE)

    screen.blit(
        text1,
        [
            (
                int(width*((2.0*column)+1.0)/6.0) -
                int(text1.get_width()/2)
            ),
            (
                int(height*((2.0*row)+1.0)/4.0) +
                int(radius/6)
            )
        ]
    )
    screen.blit(
        text2,
        [
            (
                int(width*((2.0*column)+1.0)/6.0) -
                int(text2.get_width()/2)
            ),
            (
                int(height*((2.0*row)+1.0)/4.0) +
                text1.get_height() +
                int(radius/6)
            )
        ]
    )
    pygame.draw.circle(
        screen,
        WHITE,
        [
            int(width*((2.0*column)+1.0)/6.0),
            int(height*((2.0*row)+1.0)/4.0)
        ],
        radius,
        2
    )  
    pygame.draw.rect(
        screen,
        BLUE,
        [
            int(width*((2.0*column)+1.0)/6.0)-radius,
            int(height*((2.0*row)+1.0)/4.0)-radius,
            2*radius,
            2*radius
        ],
        2
    )
    pygame.draw.line(
        screen,
        RED,
        [
            int(width*((2.0*column)+1.0)/6.0),
            int(height*((2.0*row)+1.0)/4.0)
        ],
        [
            (
                int(width*((2.0*column)+1.0)/6.0) - 
                int(radius*cos(pi/2.0*(value_pct-25.0)/25.0))
            ),
            (
                int(height*((2.0*row)+1.0)/4.0) - 
                int(radius*sin(pi/2.0*(value_pct-25.0)/25.0))
            )
        ],
        2
    )

if __name__ == "__main__":

    pygame.init()
    font = pygame.font.Font(None, 36)
 
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width = screen.get_width()
    height = screen.get_height()

    radius = int(width/6.0)
    if radius > int(height/4.0):
        radius = int(height/4.0)


    done = False

    pyobd2 = PyOBD2.PyOBD2()
    pyobd2.startInterface()

    while True:

        data = True 
        data = pyobd2.runMonitor()
        if not data:
            screen.fill(RED)
            pygame.display.flip()
            continue
        elif done:
            break
 
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done=True 
 
        screen.fill(BLACK)

        for i in range(0, 3, 1):
            for j in range(0, 2, 1):
                text_display = None
                if j == 0:
                    value_pct = data['engine_rpm']/70
                    text_display_1 = str(data['engine_rpm'])
                    text_display_2 = 'RPM'
                else:
                    value_pct = data['velocity_kph']/1.20
                    text_display_1 = str(data['velocity_kph'])
                    text_display_2 = 'KPH'
                draw_gauge(j, i, value_pct, text_display_1, text_display_2)
 
        pygame.display.flip()

    pyobd2.shutdown() 
    pygame.quit()

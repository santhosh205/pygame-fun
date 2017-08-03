import pygame
pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
window_x_length = 800
window_y_height = 600
rectangle_width = 10
rectangle_height = 10
rectangle_displacement = 10
rectangle_initial_x_coordinate = 200
rectangle_initial_y_coordinate = 200
FPS = 15
gameDisplay = pygame.display.set_mode((window_x_length,window_y_height))
pygame.display.update()
lead_x = rectangle_initial_x_coordinate 
lead_y = rectangle_initial_y_coordinate 
lead_x_change = 0
lead_y_change = 0
x_ind = 0
y_ind = 0
left = 0
right = 0
up = 0
down = 0
clock = pygame.time.Clock()
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if right == 0:
                    lead_x_change = -(rectangle_displacement)
                    x_ind = 1
                    left = 1
                    up = 0
                    down = 0
            if event.key == pygame.K_RIGHT:
                if left == 0:
                    lead_x_change = rectangle_displacement
                    x_ind = 1
                    right = 1
                    up = 0
                    down = 0
            if event.key == pygame.K_UP:
                if down == 0:
                    lead_y_change = -(rectangle_displacement)
                    y_ind = 1
                    up = 1
                    left = 0
                    right = 0
            if event.key == pygame.K_DOWN:
                if up == 0:
                    lead_y_change = rectangle_displacement
                    y_ind = 1
                    down = 1
                    left = 0
                    right = 0
            if event.key == pygame.K_SPACE:
                lead_x_change = 0
                lead_y_change = 0
    if lead_x >= window_x_length or lead_y >= window_y_height or lead_x <= 0 or \
                            lead_y <= 0:
        gameExit = True
    if x_ind == 1:
        lead_y_change = 0
    if y_ind == 1:
        lead_x_change = 0
    lead_x += lead_x_change
    lead_y += lead_y_change
    x_ind = 0
    y_ind = 0
    gameDisplay.fill(white)
    gameDisplay.fill(black, rect=[lead_x,lead_y,rectangle_width,rectangle_height])
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()

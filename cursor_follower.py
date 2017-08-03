import pygame
pygame.init()
white = (255,255,255)
black = (0,0,0)
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.update()
lead_x = 200
lead_y = 200
lead_x_change = 0
lead_y_change = 0
direction = 0
clock = pygame.time.Clock()
FPS = 60
gameExit = False
def getMousePos():
    return pygame.mouse.get_pos()
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    mousePosition = getMousePos()
    x_distance = mousePosition[0] - lead_x
    y_distance = mousePosition[1] - lead_y
    modx = abs(x_distance)
    mody = abs(y_distance)
    if mody < 10 or modx < mody:
        if x_distance >= 10:
            lead_x_change = 10
        elif x_distance > -10 and x_distance < 10:
            lead_x_change = x_distance
        elif x_distance <= -10:
            lead_x_change = -10
    if modx < 10 or mody < modx:
        if y_distance >= 10:
            lead_y_change = 10
        elif y_distance > -10 and y_distance < 10:
            lead_y_change = y_distance
        elif y_distance <= -10:
            lead_y_change = -10
    lead_x += lead_x_change
    lead_y += lead_y_change
    lead_x_change = 0
    lead_y_change = 0
    if lead_x >= 790 or lead_x <= 0:
        lead_x_change = 0
        if lead_x > 790:
            lead_x -= 10
        if lead_x < 0:
            lead_x += 10
    if lead_y >= 590 or lead_y <= 0:
        lead_y_change = 0
        if lead_y > 590:
            lead_y -= 10
        if lead_y < 0:
            lead_y += 10
    gameDisplay.fill(white)
    gameDisplay.fill(black, rect=[lead_x,lead_y,10,10])
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()

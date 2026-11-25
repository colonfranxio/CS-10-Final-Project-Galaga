import pygame

#initial set up
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

#PLAYER SET UP
Player = pygame.image.load("ship.png")
speed = 5
x = 400
y = 500

#this bit basically starts up the game
running = True 
while running: 
    #set up the screen
    screen.fill((0,0,0))

    #display player
    screen.blit(Player, (x, y))
    pygame.display.flip()

    ###tracks events 
    for event in pygame.event.get():
    ##makes it easier to quit lol
        if event.type == pygame.QUIT:
            running = False

    #updates game state by grabbing the recently pressed keys##
    keys = pygame.key.get_pressed()

    ##Player Movement/Shooting 

    if keys[pygame.K_LEFT]:
         x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed

    ##Game Over 

    ###Enemy logic 

    ##High score 

    ## frame rate
    clock.tick(60)
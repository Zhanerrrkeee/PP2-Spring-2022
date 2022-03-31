from turtle import st
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))
running = True
x = y = 50
step = 20
clock = pygame.time.Clock()
pygame.display.set_caption("Ball")
while running:
    if x > 1280: x = 1255
    elif x < 0: x = 25
    elif y > 720: y = 695
    elif y < 0: y = 25    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()        
    if pressed[pygame.K_UP]: y -= step
    elif pressed[pygame.K_DOWN]: y += step
    elif pressed[pygame.K_LEFT]: x -= step
    elif pressed[pygame.K_RIGHT]: x += step
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),(x,y),(25))
    
    clock.tick(60)
    pygame.display.update()
pygame.quit()               

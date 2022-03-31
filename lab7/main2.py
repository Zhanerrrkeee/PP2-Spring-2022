import pygame

#init 
pygame.init()

#display
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("MP3 Player v2.0")
running = True

#clock
clock = pygame.time.Clock()
#music
cnt = 0
song = ['Tokyo Ghoul Opening 1','Atack on Titan Opening S2','Death Note Opening 1' ,'Black Clover Opening 10']
mus = ['music\ghoul.mp3','music\_atack_on_titan.mp3','music\death_note.mp3','music\_black_clover.mp3']
#buttons and background
background = ['fon\_tokyo_ghoul.jpg','fon\_atack_on_titan.jpg','fon\death_note.jpg','fon\_black_clover.png']
play_button = pygame.image.load('icon\_1pause.png').convert_alpha()
pause_button = pygame.image.load('icon\pause.png').convert_alpha()
next_button = pygame.image.load('icon\_newnext.png').convert_alpha()
previous_button = pygame.image.load('icon\previous.png').convert_alpha()
#text
font = pygame.font.SysFont('Times New Roman',25)
rem = True
mainmenu = True
#program
while running:
    #name of the songs
    # text = font.render(song[cnt],True,(255,255,255))
    x,y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        #quit the program
        if event.type == pygame.QUIT:
            running = False
        #binds     
        elif rem and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 560 < x < 760  and 450 < y < 650 :
            mainmenu = False
            rem = False
            pygame.mixer.music.load(mus[cnt])
            pygame.mixer.music.play(0)
            screen.blit(pygame.image.load(background[cnt]).convert(),(0,0))
            screen.blit(font.render(song[cnt],True,(255,255,255)),(500,0))    
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and rem == False and 560 < x < 760  and 450 < y < 650:
                pygame.mixer.music.stop()
                rem = True
        # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and cnt <= 0 and 360 < x < 560 and 450< y < 650:
            # rem = False
            # cnt = 0
            # pygame.mixer.music.load(mus[cnt])
            # screen.blit(pygame.image.load(background[cnt]).convert(),(0,0))
            # pygame.mixer.music.play(0)
        # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1  and cnt >= 3 and 360 < x < 560 and 450< y < 650:
            # rem = False
            # cnt = 3
            # pygame.mixer.music.load(mus[cnt])
            # screen.blit(pygame.image.load(background[cnt]).convert(),(0,0))
            # pygame.mixer.music.play(0)    
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 760 <x< 960 and 450<y<650 :
            cnt += 1
            pygame.mixer.music.load(mus[cnt])
            pygame.mixer.music.play(0)
            screen.blit(pygame.image.load(background[cnt]).convert(),(0,0))
            screen.blit(font.render(song[cnt],True,(255,255,255)),(500,0))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 360<x<560 and 450<y<650:
            cnt -= 1
            pygame.mixer.music.load(mus[cnt])
            pygame.mixer.music.play(0)
            screen.blit(pygame.image.load(background[cnt]).convert(),(0,0))
            screen.blit(font.render(song[cnt],True,(255,255,255)),(500,0))

    #main screen
    if mainmenu:
        screen.blit(pygame.image.load(background[0]).convert(),(0,0))
     
    if rem:
        screen.blit(pygame.image.load(background[cnt]).convert(),(0,0))
        screen.blit(play_button,(560,450))
    else:
        
        screen.blit(pause_button,(560,450))            
    if cnt == 0:
        screen.blit(next_button,(760,450))
    if cnt == 3:
        screen.blit(previous_button,(360,450))
    if 0 < cnt < 3:
        screen.blit(previous_button,(360,450))
        screen.blit(next_button,(760,450))
    #change name of the songs
    # pressed = pygame.key.get_pressed()
    # if pressed[pygame.MOUSEBUTTONDOWN] and event.button == 1 and 560 < x < 760  and 450 < y < 650:
    #     screen.blit(text,(500,0))
    # if pressed[pygame.MOUSEBUTTONDOWN]:
    #     screen.blit(text,(500,0))
    # if pressed[pygame.MOUSEBUTTONDOWN]:
    #     screen.blit(text,(500,0))         
    pygame.display.update()       
    #fps
    clock.tick(60)      
              
pygame.quit()
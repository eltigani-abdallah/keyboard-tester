import pygame
pygame.init()

screen=pygame.display.set_mode((500,100))

run=True

while run:
    events=pygame.event.get()
    keys=pygame.key.get_pressed()
    for event in events:
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            print(f"key:{event.unicode} name: {pygame.key.name(event.key)}")

    pygame.display.flip()

pygame.quit()
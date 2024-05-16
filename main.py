import pygame

pygame.init()

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1800

screen =pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player1 = pygame.Rect((300, 250, 50, 50))
player2 = pygame.Rect((400, 400, 50, 50))

run = True
while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), player1)

    pygame.draw.rect(screen, (192, 65, 120), player2)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player1.move_ip(-2, 0)
    if key[pygame.K_d]:
        player1.move_ip(2, 0)
    if key[pygame.K_w]:
        player1.move_ip(0, -2)
    if key[pygame.K_s]:
        player1.move_ip(0, 2)

    if player1.left < 10:
        player1.left = 1780

    if player1.right > 1790:
        player1.right = 20

    if player1.top < 0:
        player1.top = 1780

    if player1.bottom > 1800:
        player1.bottom = 20


    if key[pygame.K_UP]:
        player2.move_ip(0, -1)
    if key[pygame.K_DOWN]:
        player2.move_ip(0, 1)
    if key[pygame.K_LEFT]:
        player2.move_ip(-1, 0)
    if key[pygame.K_RIGHT]:
        player2.move_ip(1, 0)

    if player2.left < 0:
        player2.left = 1780

    if player2.right > 1800:
        player2.right = 20

    if player2.top < 0:
        player2.top = 1780

    if player2.bottom > 1800:
        player2.bottom = 20


    if player1.colliderect(player2):
        print("Game over")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()





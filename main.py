import pygame

pygame.init()

WDT = 500
HGHT = 500

WIN = pygame.display.set_mode((WDT, HGHT))
pygame.display.set_caption("First Pygame Game!")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = y = 350
width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

run = True

def redrawGameWindow():
    global walkCount
    WIN.blit(bg, (0, 0))
    
    if walkCount + 1 >= 27:
        walkCount = 0
    
    if left:
        WIN.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        WIN.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        WIN.blit(char, (x, y))

    pygame.display.update()

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x - vel >= 0:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x + vel <= WDT - width:
        x += vel
        left = False
        right = True
    else:
        right = left = False
        walkCount = 0
    
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = right = False
    
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    
    redrawGameWindow()
    
pygame.quit()

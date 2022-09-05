import pygame


pygame.init()

blockSize = 100


nx = int(input())
ny = int(input())

ax = nx+1
ay = ny+1

x = 100*nx
y = 100*ny

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
win_w = 1000

widht = 100
height = 100

win = pygame.display.set_mode((win_w, 1000))

pygame.display.set_caption("Conway's Game of Life")

alive = [(nx,ny)]


#--------// Functions //------------------------------------------------------------------

def drawGrid():
    for x in range(0, win_w, blockSize):
        for y in range(0, win_w, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(win, BLACK, rect, 1)

#--------// Colisions//------------------------------------------------------------------

def draw():

    for i in alive:
            s = str(i).replace('(','').replace(')','').split(', ') 
            [ax, ay] = s
            x = blockSize*(int(ax)-1)
            y = blockSize*(int(ay)-1)  
            pygame.draw.rect(win, (0, 0, 0), (x, y, blockSize, blockSize))


#--------------------------------------------------------------------------


run = True

while run:
    pygame.time.delay(1000)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    
    win.fill((255, 255, 255))
    drawGrid()
    draw()

    s = [ax, ay]
    ax = int(ax)-1
    ay = int(ay)-1
    alive.append((ax-1, ay-1))
    print(alive)
    
    pygame.display.update()


pygame.quit() 

















































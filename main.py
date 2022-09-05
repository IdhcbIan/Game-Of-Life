import pygame


pygame.init()

blockSize = 20



nx = 5
ny = 5

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

alive = [(5,5), (5,6), (6,5), (6,6)]

vizinhos = []


#--------// Functions //------------------------------------------------------------------

def drawGrid():
    for x in range(0, win_w, blockSize):
        for y in range(0, win_w, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(win, BLACK, rect, 1)

#--------// All //------------------------------------------------------------------


all = []

def count(): 
    w = 0
    h = 0 
    cx = 1
    cy = 1
    while h <1000:
        if w < 1000:
            all.append((cx,cy))
            cy += 1
            w += blockSize
        elif h < 1000:
            cx += 1
            w = 0
            h += blockSize
            cy = 0
            cy += 1
        else:
            pass
 
    
#--------// Colisions//------------------------------------------------------------------

def draw():

    for i in alive:
            s = str(i).replace('(','').replace(')','').split(', ') 
            [ax, ay] = s
            x = blockSize*(int(ax)-1)
            y = blockSize*(int(ay)-1)  
            pygame.draw.rect(win, (0, 0, 0), (x, y, blockSize, blockSize))

#--------// Rules//------------------------------------------------------------------
pr_in = []
pr_out = []

def vis():
  for i in all:
        s = str(i).replace('(','').replace(')','').split(', ') 
        [fx, fy] = s
        fx = int(fx)
        fy = int(fy)
        vizinhos = [(fx-1, fy+1), (fx, fy+1), (fx+1, fy+1), (fx-1, fy), (fx+1, fy), (fx-1, fy-1), (fx, fy-1), (fx+1, fy-1) ]

        s = sum(vs in vizinhos for vs in alive)
        #print(s)

        if i in alive:
            if s >= 4:
                pr_out.append(i)
            elif s <= 2:
                pr_out.append(i)
            elif s == 2 or s == 3:
                pass
        else:
            if s == 3:
                pr_in.append(i)
            else:
                pass

def compare():
    for i in pr_out:
        try:
            alive.remove(i)
        except ValueError:
            pass
    for i in pr_in:
        if i not in alive:
            alive.append(i)

#--------------------------------------------------------------------------

count()
#print(all)

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
    ax = int(ax)
    ay = int(ay)
    alive.append((ax-1, ay-1))
    
    vis()
    compare()
    pygame.display.update()


pygame.quit() 

#--------------------------------------------------------------------------





    







































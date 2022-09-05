
#++++++++++++++++ // Ptgame tutorial  //+++++++++++++++++++++++++++++
import pygame
#       //  pygame tutorial 1  //

"""
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")


x = 50
y = 50
widht = 40
height = 60
vel = 5


run = True

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        x -= vel
        print('left')
    if keys[pygame.K_RIGHT]:
        x += vel
        print('right')
    if keys[pygame.K_UP]:
        y -= vel
        print('up')
    if keys[pygame.K_DOWN]:
        y += vel
        print('down')
    
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, widht, height))  #creates the character
    pygame.display.update()


pygame.quit() 
"""
#-----------------------------------------  #making the program close
"""
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
"""


#///////////////////////////////////////////////////////////


#       // Pygame tutorial 2 // #making the borther of the window

"""

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")


x = 50
y = 50
widht = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        print('left')
    if keys[pygame.K_RIGHT] and x < 500 - widht - vel:
        x += vel
        print('right')
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
            print('up')
        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
            print('down')
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) / 2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10




    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, widht, height))
                       # creates the character
    pygame.display.update()


pygame.quit()


"""


#///////////////////////////////////////////////////////



#       // Character Animation & Sprites  //


"""

pygame.init()

win = pygame.display.set_mode((852, 480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('back.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = 10
y = 411
widht = 64
height = 64
vel = 5

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

#----------------------------------------------

def redraGameWindow():
    global walkCount

    win.blit(bg, (0, 0))   #makea the backgrond the png
    
    # creates the character

    if walkCount + 1 >= 27:
        walkCount = 0


    if left: 
        win.blit(walkLeft[walkCount//3], (x,y))  #integer removes, divides with no rest
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))  # integer removes, divides with no rest
        walkCount += 1
    else:
        win.blit(char, (x,y))

    pygame.display.update()

#-----------------------------
#// Main Loop  //-------------------------------------------------

run = True
while run:
    clock.tick(27)   #set fpf to 27

    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and x > vel:  #// Left
        x -= vel
        right = False
        left = True
        print('left')

    elif keys[pygame.K_RIGHT] and x < 500 - widht - vel: #// Right
        x += vel
        right = True
        left = False
        print('right')

    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:  #// Jump
            isJump = True
            right = False
            left = False
            walkCount = 0
            print('Jump')
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) / 2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redraGameWindow()  #calling function
#end of main loop

#//
pygame.quit()
#//

"""



#////////////////////////////////////////////////////////////





#       // Optimization  //


pygame.init()

win = pygame.display.set_mode((852, 480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load(
    'R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load(
    'L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('back.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, widht, height):
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
           # creates the character
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            # integer removes, divides with no rest
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:  
            # integer removes, divides with no rest
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))


#----------------------------------------------
"""

def redraGameWindow():
    

    win.blit(bg, (0, 0))  # makea the backgrond the png
    man.draw(win)    #calls canvas draw

    pygame.display.update()

#-----------------------------
#// Main Loop  //-------------------------------------------------

man = player(10, 411, 64, 64)    # call the class passig the atributes 
run = True
while run:
    clock.tick(27)  # set fpf to 27    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:  # // Left
        man.x -= man.vel
        man.right = False
        man.left = True
        print('left')

    elif keys[pygame.K_RIGHT] and man.x < 852 - man.widht - man.vel:  # // Right
        man.x += man.vel
        man.right = True
        man.left = False
        print('right')

    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if not(man.isJump):
        if keys[pygame.K_SPACE]:  # // Jump
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
            print('Jump')
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) / 2 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redraGameWindow()  # calling function
#end of main loop

#//
pygame.quit()
#//

"""

#/////////////////////////////////////////////////////////////////////////////////////




#       //  Projectiles  //


pygame.init()

win = pygame.display.set_mode((1000, 480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load(
    'R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load(
    'L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('back.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


#mainloop
man = player(200, 410, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 1000 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width // 2),
                                      round(man.y + man.height//2), 6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 1000 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()




















#++++++++++++++++++++++++++++++++++++++++++++++++++++++//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

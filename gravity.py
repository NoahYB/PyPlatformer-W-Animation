import pygame
pygame.init()
clock = pygame.time.Clock()
width = 600
height = 600
screen = pygame.display.set_mode((width,height))
game = True
CYAN = (0,255,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
isJump = False
horiz = 10
counter = 0
t_r = .5
t_l = .5
acc = 2
acc_l = 2
t_2 = 0
#CONTROLLABLE BLOCK

class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):

        super().__init__()
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width,height])

        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.rect.y = self.rect.bottom

    def update_right(self):
        global t_r
        global acc
        if acc < 16:
            acc = (t_r**1.09)*.8
        
        elif acc>16:
            acc = 16
        t_r += 1
        #print(acc)

        
        if self.rect.x < (width-20):
            self.rect.x += acc
        else:
            self.rect.x = width-20
    def update_left(self):
        global t_l
        global acc_l
        if acc_l < 16:
            acc_l = (t_l**1.09)*.8
            
        elif acc>16:
            acc_l = 16
        t_l += 1
        #print(acc_l)

        
        if self.rect.x >= 0+20:
            self.rect.x -= acc_l
        else:
            self.rect.x = 0
    def gravity(self):
        global t_2
        global acc_2
       
        if t_2 < 1:
            t_2 +=1
        if t_2 < 8:
            acc_2 = (t_2 **2)*.25 
            t_2 += 1
        if t_2 >= 8:
            acc_2 = (t_2**2)*.25
        
        self.rect.y += acc_2
            
        

#PLATFORMS
class Platform(pygame.sprite.Sprite):
    def __init__(self,color,width,height):

        super().__init__()
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width,height])

        self.image.fill(color)

        self.rect = self.image.get_rect()
    
#player specifics
player = Block(CYAN,30,30)
player_list = pygame.sprite.Group()
player_list.add(player)
player.rect.x = 50
player.rect.bottom = 300



#platform specifics
platform1 = Platform(WHITE,100,90)
platform_list = pygame.sprite.Group()
platform_list.add(platform1)
platform1.rect.x = 400
platform1.rect.y = 300

platform2 = Platform(WHITE, 100, 90)
platform_list.add(platform2)
platform2.rect.x = 30
platform2.rect.y = 60

ground = Platform(WHITE,600,30)
platform_list.add(ground)
ground.rect.x = 0
ground.rect.y = 570
#MOVEMENT and Gravity
velocity = 5

isJump = False

neg = 0
isLeft = False
isRight = False
isFalling = True
while game:
    
    isFalling = True
    
    screen.fill((BLACK))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            
    key = pygame.key.get_pressed()

    if key[pygame.K_RIGHT]:
        isRight= True
        player.update_right()
    if key[pygame.K_LEFT]:
        isLeft = True
        player.update_left()
    if isLeft == False and isRight == False:
        acc_l = 2
        acc = 2
        t_r = 2
        t_l =2
    if isJump == False:
        horiz = 10

    
    
    if pygame.sprite.spritecollideany(player, platform_list):
        isFalling = False
        twent = pygame.sprite.spritecollideany(player, platform_list)
        player.rect.bottom = twent.rect.top+2
        if key[pygame.K_SPACE]:
            isJump = True
    if isJump == True:
        isFalling = False
        if horiz >= -10:
            neg = 1
            if horiz < 0:
                neg = -1
            vert = (horiz ** 2) *.8* neg 
            
            player.rect.y -= vert
            
            

            horiz -= 1
        else:
            horiz = 10
            isJump = False
    
    isLeft = False
    isRight = False
    if isFalling:
        player.gravity()
    player_list.draw(screen)
    platform_list.draw(screen)
    
    pygame.display.flip()
    
    
    clock.tick(60)
pygame.quit()


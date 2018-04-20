
import pygame
import time
pygame.init()
sprite_list = ['sprite2.png','sprite4.png','sprite5.png','sprite6.png']
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,600))
black = (255,255,255)
limit = len(sprite_list)
game = True
a = 0
i = 0
j = 0
lr = 10
up = 10
s = 0

WHITE = (255,255,255)


class Player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        
        self.frame = 0
        
        self.image = pygame.image.load(sprite_list[self.frame]).convert()
        
        self.image.set_colorkey((255,255,255))

        self.rect = self.image.get_rect()
    def update(self):
        global a
        if a == 10:
            if self.frame < len(sprite_list) -1:
                self.frame += 1
                self.image = pygame.image.load(sprite_list[self.frame])
            if self.frame == len(sprite_list) -1:
                self.frame = 0
                self.image = pygame.image.load(sprite_list[self.frame])
            a = 0
        if a < 10:
            a += 1
class Platform(pygame.sprite.Sprite):
    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
def anim_stall():
    global a
    global i
    if i >= 0 and i < 5:
        i += 1
    if i >= 5:
        a += 1
        i = 0
    if a > (len(sprite_list)-1):
        a = 0
screen.fill(black)

platform_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
all_sprite = pygame.sprite.Group()


platform = Platform((0,0,0), 200, 10)
ground = Platform((0,0,0), 600, 10)
platform.rect.x = 20
platform.rect.y = 200
ground.rect.x = 0
ground.rect.y = 580

platform_list.add(platform)
platform_list.add(ground)
all_sprite.add(platform)
all_sprite.add(ground)

player = Player()
player.rect.x = 20
player.rect.y = 20

all_sprite.add(player)
player_list.add(player)
key = pygame.key.get_pressed()


while game:
    right_press = False
    space_press = False
    right_hold = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right_press = True
            if event.key == pygame.K_SPACE:
                player.rect.y -= 90
            
                
            
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            player.rect.x += 2
            player.update()
            
            
        if event.key == pygame.K_LEFT:
            player.rect.x -= 2
            player.update()
    

        
            
    standing_on = pygame.sprite.groupcollide(player_list, platform_list, 0,0)
    player.rect.y += 4
    for player in standing_on:
        player.rect.y -= 4
    screen.fill(WHITE)
    all_sprite.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

import pygame
import os
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Tutorial")

# Load images
RED_GHOST = pygame.transform.scale(pygame.image.load(os.path.join("assets", "ghost.png")), (27, 27))
GREEN_GHOST = pygame.transform.scale(pygame.image.load(os.path.join("assets", "ghost1.png")), (27, 27))
BLUE_GHOST = pygame.transform.scale(pygame.image.load(os.path.join("assets", "ghost2.png")), (27,27))

# Player player
PAC = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pacman.png")), (30, 30))
PAC1=pygame.transform.rotate(PAC,180)
DOT=pygame.transform.scale(pygame.image.load(os.path.join("assets", "download.png")), (25, 25))
# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "converted.png")), (WIDTH, HEIGHT))
BG1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


class Pacca:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(img)
        self.img = img

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))


class Ghost(Pacca):
    c = 3

    def move(self):
        c = self.c
        if collisionb(bg, self, c,enemy_vel) == True:
            if c == 1:
                self.x -= enemy_vel
            if c == 2:
                self.x += enemy_vel
            if c == 3:
                self.y -= enemy_vel
            if c == 4:
                self.y += enemy_vel
        else:
            if c == 1 or c == 2:
                self.c = random.randrange(3, 5)
            elif c == 3 or c == 4:
                self.c = random.randrange(1, 3)


class Player(Pacca):
    pass

def collide(obj1,obj2):
    offset_x = int(obj2.x - obj1.x)
    offset_y = int(obj2.y - obj1.y)
    if obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None:
        return True
    else:
        return False

def collisionb(obj1, obj2, no,vel):
    offset_x = int(obj2.x - obj1.x)
    offset_y = int(obj2.y - obj1.y)
    if no == 1:
        if obj1.mask.overlap(obj2.mask, (offset_x - vel, offset_y)) != None:
            return False
        else:
            return True
    if no == 2:
        if obj1.mask.overlap(obj2.mask, (offset_x + vel, offset_y)) != None:
            return False
        else:
            return True
    if no == 3:
        if obj1.mask.overlap(obj2.mask, (offset_x, offset_y - vel)) != None:
            return False
        else:
            return True
    if no == 4:
        if obj1.mask.overlap(obj2.mask, (offset_x, offset_y + vel)) != None:
            return False
        else:
            return True
    if no==0:
        if obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None:
            return False
        else:
            return True

player_vel = 5
enemy_vel = 3
lives=3
player = Player(320, 650, PAC)
bg = Player(0, 0, BG)
clock = pygame.time.Clock()
main_font = pygame.font.SysFont("comicsans", 50)
lost_font = pygame.font.SysFont("comicsans", 60)
FPS = 60
ghosts = []
dots=[]


def redraw_window():
    a = len(dots)
    lives_label = main_font.render(f"Lives: {a}", 1, (255, 255, 255))
    level_label = main_font.render(f"Level: 1", 1, (255, 255, 255))
    WIN.blit(BG1, (0, 0))
    WIN.blit(BG, (0, 0))
    WIN.blit(lives_label, (10, 10))
    WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

    for ghost in ghosts:
        ghost.draw(WIN)
    player.draw(WIN)
    pygame.display.update()


run = True
k=0
while run:
    if lives ==0:
        break
    clock.tick(FPS)
    redraw_window()
    k+=1
    if len(ghosts)<3 and k>240:
        k=0
        for i in range (1):
            ghost = Ghost(WIDTH / 2 - 12, 320,random.choice([RED_GHOST,GREEN_GHOST,BLUE_GHOST ]))
            ghosts.append(ghost)
    for ghost in ghosts:
        ghost.move()
        if collide(player,ghost):
            lives-=1
            ghosts.remove(ghost)

    keys = pygame.key.get_pressed()

    if player.x <0:
        player.x=WIDTH+player.x
    if player.x >WIDTH:
        player.x=player.x-WIDTH
    if keys[pygame.K_a] and collisionb(bg, player, 1,player_vel):  # left
        player.x -= player_vel
        player=Player(player.x,player.y,PAC1)
    if keys[pygame.K_d] and collisionb(bg, player, 2,player_vel):  # right
        player.x += player_vel
        player = Player(player.x, player.y, PAC)
    if keys[pygame.K_w] and collisionb(bg, player, 3,player_vel):  # up
        player.y -= player_vel
    if keys[pygame.K_s] and collisionb(bg, player, 4,player_vel):  # down
        player.y += player_vel
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

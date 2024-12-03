import pygame
import random
import time

from pygame.sprite import _Group
pygame.init()

screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width,screen_height])

def change_bg(img):
    bg = pygame.image.load(img)
    bg = pygame.transform.scale(bg, (900,700))
    screen.blit(bg, (0,0))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()

class NonRecyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plastic.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

item_list = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

bin = Bin()
all_sprites.add(bin)

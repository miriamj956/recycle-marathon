import pygame
import random
import time

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

images = ["item1.png", "item2.png", "item3.png"]

for i in range(50):
    item = Recyclable(random.choice(images))
    item.rect.x = random.randrange(screen_width)
    item.rect.y = random.randrange(screen_height)
    item_list.add(item)
    all_sprites.add(item)

for i in range(20):
    plastic = NonRecyclable()
    plastic.rect.x = random.randrange(screen_width)
    plastic.rect.y = random.randrange(screen_height)
    plastic_list.add(plastic)
    all_sprites.add(plastic)

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

playing = True
score = 0

clock = pygame.time.Clock()
start_time = time.time()

myFont = pygame.font.SysFont("Ariel", 22)
text = myFont.render("Score =" +str(0), True, black)

while playing:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    timeElapsed = time.time()-start_time
    if timeElapsed >= 60:
        if score >= 20:
            screen.fill("green")
            text = myFont.render("You Win!", True, black)
        else:
            screen.fill(red)
            text = myFont.render("You Lose!", True, black)
        screen.blit(text, (250,40))
    else:
        change_bg("bground.png")
        countDown = myFont.render("Time Left:" +str(60 - int(timeElapsed)), True, white)
        screen.blit(countDown, (20,10))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y > 0:
                bin.rect.y -= 5
        if keys[pygame.K_DOWN]:
            if bin.rect.y < screen_height - 50:
                bin.rect.y += 5
        if keys[pygame.K_LEFT]:
            if bin.rect.x > 0:
                bin.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            if bin.rect.x < screen_width - 50:
                bin.rect.x += 5

        item_hit_list = pygame.sprite.spritecollide(bin, item_list, True)
        plastic_hit_list = pygame.sprite.spritecollide(bin, plastic_list, True)
        for item in item_hit_list:
            score += 1 
            text = myFont.render("Score: " +str(score), True, red)
        for plastic in plastic_hit_list:
            score -= 5 
            text = myFont.render("Score: " +str(score), True, red)
    screen.blit(text, (20, 50))
    all_sprites.draw(screen)
    pygame.display.update()

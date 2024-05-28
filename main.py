import pygame
import random

import self
from pygame.examples.aliens import (Player)

WIDTH = 600
HEIGHT = 800
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Метеоритный дождь")

clock = pygame.time.Clock()

class Meteor(pygame.sprite.Sprite):

   def __init__(self): pygame.sprite.Sprite.__init__(self)

self.image = pygame.Surface((30, 40))

self.image.fill((255, 0, 0))

self.rect = self.image.get_rect()

self.rect.x = random.randint(0, WIDTH - self.rect.width)

self.rect.y = random.randint(-100, -40)

self.speedy = random.randint(1, 15)

all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(8):
  m = Meteor()
  all_sprites.add(m)
  meteors.add(m)

score = 0

import pygame
import math
from random import randint

SPRITE = "gfx/bug.png"
SIZE = 25
SPEED = 0.015

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy, self).__init__()

        self.x, self.y = self.__random_spawn()
        self.vx, self.vy = self.__random_vector()

        vector_x, vector_y = self.vx - self.x, self.vy - self.y
        self.angle = math.degrees(math.atan2(-vector_y, vector_x))

        self.rect = pygame.Rect(self.x, self.y, SIZE, SIZE)

        self.image = pygame.image.load(SPRITE).convert_alpha()
        self.image = pygame.transform.rotate(self.image, self.angle - 90)
        self.image = pygame.transform.scale(self.image, (SIZE, SIZE))

    def show (self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def update (self) -> None:
        self.x += self.vx * SPEED
        if self.x < 0:
            self.x = 550
        elif self.x > 550:
            self.x = 0
        self.y += self.vy * SPEED
        if self.y < 100:
            self.y = 650
        elif self.y > 650:
            self.y = 100

        self.rect.left, self.rect.top = self.x, self.y

    def __random_spawn(self) -> tuple:
        ORIGINS = {0: "up", 1: "down", 2: "left", 3: "right"}
        origin = randint(0,3)
        if ORIGINS[origin] == "up":
            return (randint(150,600), 0)
        elif ORIGINS[origin] == "down":
            return (randint(150,600), 550)
        elif ORIGINS[origin] == "left":
            return (150, randint(0, 550))
        elif ORIGINS[origin] == "right":
            return (660, randint(0, 550))
    
    def __random_vector (self) -> tuple:
        return (50 + (randint(0,9) * 50), 50 + (randint(0,9) * 50))
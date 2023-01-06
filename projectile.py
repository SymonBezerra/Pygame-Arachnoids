import pygame

SPRITE = "gfx/web_projectile.png"
SIZE = 50

class Projectile(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, angle: tuple):
        super(Projectile, self).__init__()

        self.x, self.y = x, y
        self.rect = (x, y, 50, 10)
        self.color = (140, 82, 255) # same color as the spider

        self.image = pygame.image.load(SPRITE).convert_alpha()
        self.image = pygame.transform.rotate(self.sprite, angle - 90)
        self.image = pygame.transform.scale(self.image, (SIZE, SIZE))

    def show (self, screen: pygame.Surface) -> None:
        pygame.draw.rect (screen, self.color, screen)

    def update (self) -> None:
        pass
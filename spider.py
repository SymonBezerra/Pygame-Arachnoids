import pygame

SPRITES = {"up": "gfx/spider_up.png",
"down": "gfx/spider_down.png",
"left": "gfx/spider_left.png",
"right": "gfx/spider_up.png"}

SIZE = 50
class Spider (pygame.sprite.Sprite):
    
    def __init__ (self):
        super(Spider, self).__init__()

        self.x, self.y = 250, 250

        self.direction = "down"

        self.image = pygame.image.load(SPRITES["down"]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SIZE, SIZE))
        self.rect = pygame.Rect(self.x, self.y, SIZE, SIZE)

    def show (self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def refresh (self, direction: str) -> None:
        if direction == "up":
            self.image = pygame.transform.rotate(self.image, 180)
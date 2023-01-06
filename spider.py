import pygame

SPRITE = "gfx/spider_down.png"

SIZE = 50
class Spider (pygame.sprite.Sprite):
    
    def __init__ (self):
        super(Spider, self).__init__()

        self.x, self.y = 250, 250

        self.direction = "down"

        self.sprite = pygame.image.load(SPRITE).convert_alpha()
        self.image = pygame.transform.scale(self.sprite, (SIZE, SIZE))
        self.rect = pygame.Rect(self.x, self.y, SIZE, SIZE)

    def show (self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def update (self, direction: str, angle: float = 0) -> None:
        # angle just used for mouse clicking rotation

        # rotating the image
        if self.direction != direction:
            self.rotate(direction, angle)
        # updating the direction
        self.direction = direction 

        if direction == "up" and self.y > 50:
            self.y -= SIZE
            
        elif direction == "down" and self.y < 550:
            self.y += SIZE

        elif direction == "left" and self.x > 150:
            self.x -= SIZE

        elif direction == "right" and self.x < 650:
            self.x += SIZE
        self.rect.left, self.rect.top = self.x, self.y

    def rotate(self, direction: str, angle: float) -> None:
        if direction == "up":
            self.image = pygame.transform.rotate(self.sprite, 180)
        
        elif direction == "down":
            self.image = pygame.image.load(SPRITE).convert_alpha()

        elif direction == "left":
            self.image = pygame.transform.rotate(self.sprite, 270)

        elif direction == "right":
            self.image = pygame.transform.rotate(self.sprite, 90)

        elif direction == "-":
            self.image = pygame.transform.rotate(self.sprite, angle)
        
        self.image = pygame.transform.scale(self.image, (SIZE, SIZE))
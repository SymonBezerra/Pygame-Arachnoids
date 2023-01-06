import pygame

SPRITE = "gfx/web_node.png"
SIZE = 50
class Node (pygame.sprite.Sprite):
    
    def __init__ (self, coordinate: tuple):
        super(Node, self).__init__()

        self.coordinate = coordinate
        self.visible = True

        self.image = pygame.image.load(SPRITE).convert_alpha()
        self.image = pygame.transform.scale((SIZE, SIZE))
        self.rect = pygame.Rect(self.coordinate[0], 
        self.coordinate[1], SIZE, SIZE)

    def show (self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)
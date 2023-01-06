import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, MOUSEBUTTONDOWN
from spider import Spider
# 800x600 -> 100x100px sprites -> 10x10 board = 400x400px board
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

game_spider = Spider()
if __name__ == "__main__":
    pygame.init()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        screen.fill((0,0,0)) # placeholder bg
        game_spider.show()

        pygame.display.flip()
    
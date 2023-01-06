import pygame
from pygame.locals import K_w, K_s, K_a, K_d, KEYDOWN, MOUSEBUTTONDOWN
from spider import Spider
from node import Node
# 800x600 -> 50x50px sprites -> 10x10 board = 500x50a0px board
game_screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

game_spider = Spider()
nodes = pygame.sprite.Group()
nodes.add(Node(2,4))
nodes.add(Node(2,5))
nodes.add(Node(2,3))
nodes.add(Node(3,4))
nodes.add(Node(1,4))
nodes.add(Node(1,3))
nodes.add(Node(1,5))
nodes.add(Node(3,3))
nodes.add(Node(3,5))
if __name__ == "__main__":
    pygame.init()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    game_spider.update("up", nodes)
                elif event.key == K_s:
                    game_spider.update("down", nodes)
                elif event.key == K_a:
                    game_spider.update("left", nodes)
                elif event.key == K_d:
                    game_spider.update("right", nodes)
        
        game_screen.fill((0,0,0)) # placeholder bg
        n: Node
        for n in nodes:
            if n.visible == True:
                n.show(game_screen)
        game_spider.show(game_screen)

        clock.tick(30)
        
        pygame.display.flip()
    
import pygame
import math
from pygame.locals import K_w, K_s, K_a, K_d, KEYDOWN, MOUSEBUTTONDOWN
from spider import Spider, SIZE
from projectile import Projectile
from enemy import Enemy
from node import Node
# 800x600 -> 50x50px sprites -> 10x10 board = 500x50a0px board
game_screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Arachnoids")
clock = pygame.time.Clock()

BG = pygame.image.load("gfx/background.png").convert()

game_spider = Spider()
nodes = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# initial node grid 
nodes.add(Node(2,4))
nodes.add(Node(2,5))
nodes.add(Node(2,3))
nodes.add(Node(3,4))
nodes.add(Node(1,4))
nodes.add(Node(1,3))
nodes.add(Node(1,5))
nodes.add(Node(3,3))
nodes.add(Node(3,5))

for i in range(10):
    for j in range(10):
        node = Node(i,j)
        nodes.add(node)
        if (i,j) in ((2,4), (2,5), (2,3), (3,4), (1,4), 
        (1,3), (1,5), (3,3), (3,5)): # initial grid
            node.visible = True

game_wave = 5

bullets = pygame.sprite.Group()
if __name__ == "__main__":
    pygame.init()

    wave_count = 0
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # elif event.type == KEYDOWN:
            #     if event.key == K_w:
            #         game_spider.update("up", nodes)
            #     elif event.key == K_s:
            #         game_spider.update("down", nodes)
            #     elif event.key == K_a:
            #         game_spider.update("left", nodes)
            #     elif event.key == K_d:s
            #         game_spider.update("right", nodes)
            
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                vector_x, vector_y = mouse_x - game_spider.x, mouse_y - game_spider.y
                bullet_angle = math.degrees(math.atan2(-vector_y, +vector_x))
                
                # rotating the spider
                game_spider.rotate(bullet_angle)

                # creating the Projectile
                bullets.add(Projectile(game_spider.x + SIZE // 2,
                                        game_spider.y + SIZE // 2,
                                        vector_x, vector_y,
                                        bullet_angle))

        keys = pygame.key.get_pressed()
        directions = []
        if keys[K_w] and not keys[K_s]:
            directions.append("up")
        if keys[K_s] and not keys[K_w]:
            directions.append("down")
        if keys[K_a] and not keys[K_d]:
            directions.append("left")
        if keys[K_d] and not keys[K_a]:
            directions.append("right")
    
        
        game_spider.update(directions, nodes)

        game_screen.blit(BG, (0,0))
        n: Node
        for n in nodes:
            if n.visible == True:
                n.show(game_screen)

        bullet: Projectile
        for bullet in bullets:
            if bullet.x > 800 or bullet.x < 0 or bullet.y > 600 or bullet.y < 0 or bullet.time > 50:
                bullets.remove(bullet)
            else:
                bullet.time += 1
                n: Node
                for n in nodes:
                    if bullet.rect.collidepoint(n.rect.x + 25, n.rect.y + 25):
                        n.visible = True
                
                e: Enemy
                for e in enemies:
                    if e.rect.colliderect(bullet.rect):
                        enemies.remove(e)
                bullet.update()
                bullet.show(game_screen)

        enemy: Enemy
        if len(enemies) == 0:
            if wave_count < 500:
                for i in range (game_wave): enemies.add(Enemy())
                game_wave += 5
                wave_count = 0
            else: wave_count += 1
        for enemy in enemies:
            if enemy.rect.colliderect(game_spider.rect):
                running = False
            n: Node
            for n in nodes:
                if enemy.rect.collidepoint(n.rect.x + 25, n.rect.y + 25):
                    n.visible = False
            else:
                enemy.update()
                enemy.show(game_screen)

        game_spider.show(game_screen)

        clock.tick(30)
        
        pygame.display.flip()
    
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.05
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for u in updatable:
            u.update(dt)
            
        for a in asteroids:
            if a.check_collision(player):
                # exit("Game over!")
                pass
            for bullet in shots:
                if a.check_collision(bullet):
                    a.split()
                    bullet.kill()
        
        for d in drawable:
            d.draw(screen)
              
            
        pygame.display.flip()
        exportdt = clock.tick(60) / 1000
        # print(dt)


if __name__ == "__main__":
	main()

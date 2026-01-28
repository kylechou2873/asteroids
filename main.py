import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state, log_event

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    pygame.init()
    pyClock = pygame.time.Clock()
    dt = 0
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Using Group update
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
    #init Objects
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidF = AsteroidField()
    #start game loop
    while True:
        #log state
        log_state()
        #even handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        #Background black
        screen.fill("black")
        #clock
        dt = pyClock.tick(60)/1000
        updatable.update(dt)
        #check for collide
        for a in asteroids:
            if a.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        #draw updates
        for d in drawable:
            d.draw(screen)
        #refresh
        pygame.display.flip()


if __name__ == "__main__":
    main()

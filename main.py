import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state

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
    asteroid = pygame.sprite.Group()
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroid,updatable,drawable)
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
        #draw updates
        for d in drawable:
            d.draw(screen)
        #refresh
        pygame.display.flip()


if __name__ == "__main__":
    main()

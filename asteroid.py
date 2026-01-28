from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
    def update(self, dt):
        self.position += (self.velocity * dt)
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_ang = random.uniform(20, 50)
            new_ast1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            new_ast2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            new_ast1.velocity = pygame.math.Vector2.rotate(self.velocity, rand_ang) * 1.2
            new_ast2.velocity = pygame.math.Vector2.rotate(self.velocity, -rand_ang) * 1.2
        
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS 
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shotCD = 0
    # in the Player class
    def draw(self,screen):
        #draw play on screen
        pygame.draw.polygon(screen, "white", self.triangle(), width=LINE_WIDTH)
    def rotate(self,dt):
        #rotate player
        self.rotation += PLAYER_TURN_SPEED * dt
    def move(self,dt):
        #move player adjusted to roation
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_speed_vector
    def triangle(self):
        #player unit as a triangle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shotCD -= dt
        #on key press roate
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        #on key press move
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        #on key space
        if keys[pygame.K_SPACE]:
            if self.shotCD > 0:
                pass
            else:
                self.shotCD = PLAYER_SHOOT_COOLDOWN_SECONDS 
                self.shoot()
    def shoot(self):
        shot1 = Shot(self.position.x,self.position.y,SHOT_RADIUS)
        shot1.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        

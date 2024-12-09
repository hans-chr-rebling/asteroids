import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.pos + forward * self.radius
        b = self.pos - forward * self.radius - right
        c = self.pos - forward * self.radius + right
        return [a, b, c]   

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)   

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def shoot(self):
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN   
        shot = Shot(self.pos.x, self.pos.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.pos += forward * PLAYER_SPEED * dt

    def update(self, dt):
        self.shoot_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0:
                self.shoot()    
     



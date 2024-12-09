import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.pos.x, self.pos.y), self.radius, 2) 

    def update(self, dt):
        self.pos += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        split_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS 
        
        a1 = Asteroid(self.pos.x, self.pos.y, split_asteroids_radius)
        a2 = Asteroid(self.pos.x, self.pos.y, split_asteroids_radius)

        a1.velocity = self.velocity.rotate(random_angle) * 1.2
        a2.velocity = self.velocity.rotate(-random_angle) * 1.2

        
            
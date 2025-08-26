from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        


    def draw(self, screen):
        pygame.draw.circle(screen,"white",center=self.position,radius=self.radius,width=2)
    

    def update(self, dt):
        self.position += self.velocity * dt
    

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle  = random.uniform(20,50)
        first_astro_velocity = self.velocity.rotate(angle)
        second_astro_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        astro1  = Asteroid(self.position.x,self.position.y,new_radius)
        astro2  = Asteroid(self.position.x,self.position.y,new_radius)
        astro1.velocity = first_astro_velocity * 1.2
        astro2.velocity = second_astro_velocity* 1.2
        
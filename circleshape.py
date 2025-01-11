import pygame
from constants import *
from player import *


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def detect_collision(self, other):
        distance = self.position.distance_to(other.position)
        total_radius = self.radius + other.radius
        return distance <= total_radius
    
class Shot(CircleShape):
  def __init__(self, x, y, radius, velocity):
    CircleShape.__init__(self, x, y, radius)
    self.velocity = velocity
  def update(self, dt):
    self.position += (self.velocity * dt)
  def draw(self, surface):
    pygame.draw.circle(surface, COLOR, self.position, self.radius, 2)
    
    
    
    


import pygame
import random
from constants import *
from player import *
from circleshape import *

WHITE = (255, 255, 255)

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    CircleShape.__init__(self, x, y, radius)
  def draw(self, surface):
    pygame.draw.circle(surface, WHITE, self.position, self.radius, 2)
    
  def update(self, dt):
    self.position += (self.velocity * dt)
    
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    random_angle = random.uniform(20, 50)
    new_velocity_1 = self.velocity.rotate(random_angle) * 1.2
    new_velocity_2 = self.velocity.rotate(-random_angle) * 1.2
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid_1.velocity = new_velocity_1
    new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid_2.velocity = new_velocity_2
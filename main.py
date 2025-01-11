import pygame
import sys
import random
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from circleshape import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  clock = pygame.time.Clock()
  dt = 0
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable,)
  Shot.containers = (shots, updatable, drawable) 
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()
  
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("black")
    
    for sprite in updatable:
      sprite.update(dt)
    
    for sprite in drawable:
      sprite.draw(screen)  
      
    for asteroid in asteroid_field.asteroids:
      if asteroid.detect_collision(player):
        print("Game over!")
        sys.exit()
    
    for sprite in updatable:
      shot = sprite.update(dt)
      if isinstance(sprite, Player) and shot is not None:
          shots.add(shot)
          
    for asteroid in asteroid_field.asteroids:
      for shot in shots:
        if asteroid.detect_collision(shot):
          asteroid.split()
          shot.kill()
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    
    

if __name__ == "__main__":
  main()
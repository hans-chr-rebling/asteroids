import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 

def main():
    # Initialize Pygame
    pygame.init()

    # Create a clock object
    clock = pygame.time.Clock()
    dt = 0
    
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
       
    # create groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    updatable.add(player)
    drawable.add(player)

    asteroid_field = AsteroidField()
    
    # Main game loop
    running = True
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))

        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                running = False    

        pygame.display.flip()
        
        
if __name__ == "__main__":
    main()
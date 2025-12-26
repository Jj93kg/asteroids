import pygame 
from constants import *
from logger import log_state

def main():
    print("Starting Asteroids with pygame version: {VERSION}".format(VERSION=pygame.version.ver))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.clock()
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        pygame.time.clock.tick(60)

if __name__ == "__main__":
    main()

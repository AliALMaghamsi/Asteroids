import pygame
from constants import *
def main():
    pygame.init()
    
    screen  = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    Running = True
    clock =pygame.time.Clock()
    dt=0
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,color=(0,0,0),rect=None)
        pygame.display.flip()
        dt =clock.tick(60)
        print(clock.get_fps())
        dt = dt/1000
    
if __name__ == "__main__":
    main()

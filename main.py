import physics
import pygame

class test:
    def __init__(self):
        pygame.init()


        self.rect1 = physics.DynamicRect(290, 290, 100, 100)
        self.rect2 = physics.StaticRect(500, 500, 100, 100)
        self.rect3 = physics.KinematicRect(100, 100, 100, 100)

        #start with the vels 
        self.rect1.acceleration = (50, 0)  # Move right at 50 pixels per second
        self.rect3.acceleration = (0, -50)  # Move down at 50 pixels per second

        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.dt = 0.016  # Simulate 60 FPS


    def run(self):
        while True:
            self.dt = self.clock.tick(60) / 1000.0  # Convert milliseconds to seconds
            
            self.screen.fill((255, 255, 255))

            self.rect1.update(self.dt)  # Simulate 60 FPS
            self.rect3.update(self.dt)
            

            pygame.draw.rect(self.screen, (255, 0, 0), self.rect1.get_pygame_rect())
            pygame.draw.rect(self.screen, (0, 255, 0), self.rect2.get_pygame_rect())
            pygame.draw.rect(self.screen, (0, 0, 255), self.rect3.get_pygame_rect())



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            

            pygame.display.flip()

            

if __name__ == "__main__":
    test_instance = test()
    test_instance.run()
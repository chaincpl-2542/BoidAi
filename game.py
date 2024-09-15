import pygame

class Agent:
    def __init__(self,x,y) -> None:
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.acceleration = pygame.Vector2(0,0)
        self.mess = 1
        
    def update(self):
        self.velocity = self.velocity + self.acceleration
        self.position = self.position + self.velocity
        self.acceleration = pygame.Vector2(0,0)
    
    def apply_force(self,x,y): 
        force = pygame.Vector2(x,y)
        self.acceleration = self.acceleration + (force / self.mess)
        
    
    def draw(self):
        pygame.draw.circle(screen,"red",self.position,10)

    
agent1 = Agent(300,200)
agent1.apply_force(0,1)

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

                
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("gray")
    
    agent1.update()
    agent1.draw()
           
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
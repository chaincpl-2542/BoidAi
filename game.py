import pygame
import random

WIDTH = 1280
HEIGHT = 720

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
        
        if(self.position.x > WIDTH):
            self.position.x = 0
        if(self.position.x < 0):
             self.position.x = WIDTH
        if(self.position.y > HEIGHT):
            self.position.y = 0
        if(self.position.y < 0):
             self.position.y = HEIGHT
             
    def apply_force(self,x,y): 
        force = pygame.Vector2(x,y)
        self.acceleration = self.acceleration + (force / self.mess)
        
    def draw(self):
        pygame.draw.circle(screen,"red",self.position,10)

MaxAgent = 100
agents = [Agent(random.uniform(0,WIDTH),random.uniform(0,HEIGHT)) for i in range(MaxAgent)]


#-------------Setup-------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

for agent in agents:
    agent.apply_force(random.uniform(-1,1),random.uniform(-1,1))
                
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("gray")
    
    for agent in agents:
        agent.update()
        agent.draw()
    
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
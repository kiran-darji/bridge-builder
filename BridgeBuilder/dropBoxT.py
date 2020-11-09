from Box2D import *
import pygame,sys
import math
import random

window = pygame.display.set_mode((500,500),0,32)

clock = pygame.time.Clock()
count = 0
world = b2World()
groundBody = world.CreateStaticBody(
        position=(0,-10),
        shapes=b2PolygonShape(box=(50,10)),
        )
boxes = []
#body = world.CreateDynamicBody(position=(0,20))
#box = body.CreatePolygonFixture(box=(1,1), density=1, friction=0.3)
timeStep = 1.0/50
vel_iters, pos_iters = 6,2
# This is our little game loop.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))
    count += clock.tick()
    pygame.draw.rect(window,(255,255,0),(0,450,500,50))

    if count >= 1000:
        count = 0
        body = world.CreateDynamicBody(position = (random.randint(0,1500)/100,25))
        box = body.CreatePolygonFixture(box=(1,1),density=1,friction = 0.3)
        boxes.append(body)
    
    for i in range(0,len(boxes)):
        x,y = boxes[i].position
        angle = (2*math.pi)-(boxes[i].angle - math.pi/4)
        x = 100+20*round(x)
        y = 450 - 20*round(y)
        #pygame.draw.rect(window,(250-10*i,10*i,250-10*i),(x,y,40,40))
        for j in range(0,4):
            point1 = (x+(800**0.5)*(math.cos(angle+(j*math.pi/2))),y+(800**0.5)*(math.sin(angle+(j*math.pi/2))))
            point2 = (x+(800**0.5)*(math.cos(angle+((j+1)*math.pi/2))),y+(800**0.5)*(math.sin(angle+((j+1)*math.pi/2))))
            colour = ((255-((10*(i%25)))),(255-((10*(i%25)))),(255-((10*(i%25)))))
            pygame.draw.line(window,colour,point1,point2,5)


    # Instruct the world to perform a single step of simulation. It is
    # generally best to keep the time step and iterations fixed.
    world.Step(timeStep, vel_iters, pos_iters)

    # Clear applied body forces. We didn't apply any forces, but you
    # should know about this function.
    world.ClearForces()
    pygame.display.update()
    pygame.time.wait(5)
    print(len(boxes),clock.get_fps())

    # Now print the position and angle of the body.
    #x,y = body.position
    #print (x,y, body.angle)


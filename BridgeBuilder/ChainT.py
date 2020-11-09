from Box2D import *
import pygame,sys,math

bodies = []

window = pygame.display.set_mode((400,400),0,32)
clock = pygame.time.Clock()

world = b2World()
topBody = world.CreateStaticBody(position=(20,35),shapes=b2PolygonShape(box=(20,5)))
botBody = world.CreateStaticBody(position=(20,0),shapes=b2PolygonShape(box=(20,5)))

plank = b2FixtureDef(shape=b2PolygonShape(box=(0.125,0.5)),density=20,friction=0.2)

prevBody = topBody
x = 20

for i in range(0,15):
    body = world.CreateDynamicBody(position=(x,29.5-i),fixtures=plank)

    world.CreateRevoluteJoint(bodyA=prevBody,bodyB=body,anchor=(x,30-i))

    bodies.append(body)

    prevBody = body

circle = world.CreateDynamicBody(position=(x,14),fixtures=b2FixtureDef(shape=b2CircleShape(radius=1),density=20))

world.CreateRevoluteJoint(bodyA=bodies[-1],bodyB=circle,anchor=(x,15))

timeStep = 1.0/60
vel_iters,pos_iters = 6,2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            x,y = circle.position
            if event.key == pygame.K_d:
                circle.ApplyForce(force=(20000,0), point=(x,y),wake=True)
            elif event.key == pygame.K_a:
                circle.ApplyForce(force=(-20000,0), point=(x,y),wake=True)
            elif event.key == pygame.K_w:
                circle.ApplyForce(force=(0,20000), point=(x,y),wake=True)
            elif event.key == pygame.K_s:
                circle.ApplyForce(force=(0,-2000000000), point=(x,y),wake=True)

                
    
    window.fill((0,0,0))
    pygame.draw.rect(window,(255,255,0),(0,0,400,100))

    for i in range(0,len(bodies)):
        x,y = bodies[i].position
        angle = 2*math.pi - bodies[i].angle+math.pi/2
        x = 10*x
        y = 400-10*y

        point1 = ((x+(5*math.cos(angle))),(y+5*math.sin(angle)))
        point2 = ((x-(5*math.cos(angle))),(y-5*math.sin(angle)))

        pygame.draw.line(window,(255,255,255),point1,point2)

    x,y = circle.position
    x = round(10*x)
    y = round(400-10*y)

    print(circle.angle)


    pygame.draw.circle(window,(255,255,255),(x,y),10,5)

    world.Step(timeStep,vel_iters,pos_iters)

    world.ClearForces()
    pygame.display.update()
    pygame.time.wait(5)
    clock.tick()
    #print(clock.get_fps())

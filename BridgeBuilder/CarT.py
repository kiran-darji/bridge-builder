import pygame,sys,math

from Box2D import *

window = pygame.display.set_mode((1000,400),0,32)
clock = pygame.time.Clock()

world = b2World()
groundBody = world.CreateStaticBody(position=(50,0),shapes=b2PolygonShape(box=(50,10)))
wallBody1 = world.CreateStaticBody(position=(100,20),shapes=b2PolygonShape(box=(5,20)))
wallBody2 = world.CreateStaticBody(position=(0,20),shapes=b2PolygonShape(box=(5,20)))

slope1 = world.CreateStaticBody(position=(0,0),shapes=b2EdgeShape(vertices=[(5,12),(40,10)]))
slope2 = world.CreateStaticBody(position=(0,0),shapes=b2EdgeShape(vertices=[(5,15),(35,10)]))
slope3 = world.CreateStaticBody(position=(0,0),shapes=b2EdgeShape(vertices=[(5,19),(30,10)]))
slope4 = world.CreateStaticBody(position=(0,0),shapes=b2EdgeShape(vertices=[(5,24),(25,10)]))
slope5 = world.CreateStaticBody(position=(0,0),shapes=b2EdgeShape(vertices=[(5,30),(20,10)]))

slope6 = world.CreateStaticBody(position=(100,0),shapes=b2EdgeShape(vertices=[(-5,12),(-40,10)]))
slope7 = world.CreateStaticBody(position=(100,0),shapes=b2EdgeShape(vertices=[(-5,15),(-35,10)]))
slope8 = world.CreateStaticBody(position=(100,0),shapes=b2EdgeShape(vertices=[(-5,19),(-30,10)]))
slope9 = world.CreateStaticBody(position=(100,0),shapes=b2EdgeShape(vertices=[(-5,24),(-25,10)]))
slope10 = world.CreateStaticBody(position=(100,0),shapes=b2EdgeShape(vertices=[(-5,30),(-20,10)]))


chassis = world.CreateDynamicBody(position=(50,15))
chassisDef = chassis.CreatePolygonFixture(box=(1.5,0.8),density=500,friction=0.3)

wheel1 = world.CreateDynamicBody(position=(51.5,14.20),fixtures=b2FixtureDef(shape=b2CircleShape(radius=0.8),density=1))

wheel2 = world.CreateDynamicBody(position=(48.5,14.20),fixtures=b2FixtureDef(shape=b2CircleShape(radius=0.8),density=1))

joint1 = world.CreateWheelJoint(bodyA=chassis,bodyB=wheel1,anchor=(51.5,14.2),axis=(0,1),motorSpeed=0.0,maxMotorTorque=5000.0,enableMotor=True,frequencyHz=20.0,dampingRatio=0.5,collideConnected=False)

joint2 = world.CreateWheelJoint(bodyA=chassis,bodyB=wheel2,anchor=(48.5,14.2),axis=(0,1),motorSpeed=0.0,maxMotorTorque=5000.0,enableMotor=True,frequencyHz=20.0,dampingRatio=0.5,collideConnected=False)

timeStep = 1.0/50
vel_iters,pos_iters = 10,10
forward,back = False,False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if back == False:
                    forward = True
            elif event.key == pygame.K_a:
                if forward == False:
                    back = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                forward = False
            elif event.key == pygame.K_a:
                back = False

    if forward: 
        joint2.motorSpeed = -30
        joint1.motorSpeed = -30
    elif back:
        joint2.motorSpeed = 30
        joint1.motorSpeed = 30
    elif (forward == False and back != True) or (back == False and forward != True):
        joint2.motorSpeed = 0
        joint1.motorSpeed = 0

    window.fill((0,0,0))
    pygame.draw.rect(window,(255,255,0),(0,300,1000,100))
    pygame.draw.line(window,(255,255,0),(50,400),(50,0),5)
    pygame.draw.line(window,(255,255,0),(950,400),(950,0),5)

    pygame.draw.line(window,(255,255,0),(50,280),(400,300),5)
    pygame.draw.line(window,(255,255,0),(50,250),(350,300),5)
    pygame.draw.line(window,(255,255,0),(50,210),(300,300),5)
    pygame.draw.line(window,(255,255,0),(50,160),(250,300),5)
    pygame.draw.line(window,(255,255,0),(50,100),(200,300),5)

    pygame.draw.line(window,(255,255,0),(1000-50,280),(1000-400,300),5)
    pygame.draw.line(window,(255,255,0),(1000-50,250),(1000-350,300),5)
    pygame.draw.line(window,(255,255,0),(1000-50,210),(1000-300,300),5)
    pygame.draw.line(window,(255,255,0),(1000-50,160),(1000-250,300),5)
    pygame.draw.line(window,(255,255,0),(1000-50,100),(1000-200,300),5)

    angle = 2*math.pi- chassis.angle

    x1,y1 = wheel1.position
    x1 = round(x1*10)
    y1 = round(400-y1*10)
    point3 = (x1+16*math.sin(angle),y1-16*math.cos(angle))
    point4 = (x1,y1)

    x2,y2 = wheel2.position
    x2 = round(x2*10)
    y2 = round(400-y2*10)
    point2 = (x2+16*math.sin(angle),y2-16*math.cos(angle))
    point1 = (x2,y2)

    pygame.draw.line(window,(255,255,255),point1,point2,1)
    pygame.draw.line(window,(255,255,255),point2,point3,1)
    pygame.draw.line(window,(255,255,255),point3,point4,1)
    pygame.draw.line(window,(255,255,255),point4,point1,1)
    pygame.draw.circle(window,(255,0,255),(x1,y1),8,2)
    pygame.draw.circle(window,(255,0,255),(x2,y2),8,2)

    world.Step(timeStep,vel_iters,pos_iters)

    world.ClearForces()
    pygame.display.update()
    pygame.time.wait(5)
    clock.tick()
    print(clock.get_fps())

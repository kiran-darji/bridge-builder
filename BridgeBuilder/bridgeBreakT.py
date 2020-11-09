from Box2D import *
import pygame,sys,math
import Graphics

foo = 0

window = pygame.display.set_mode((1000,600),0,32)
clock = pygame.time.Clock()

world = b2World()
dif = "easy"
land = 1

fix = b2FixtureDef(shape=b2PolygonShape(box=(17/2,5)),friction=0.2,categoryBits=0x0002,maskBits=0x0004)
groundBody1 = world.CreateStaticBody(position=(17/2,5),fixtures = fix)
groundBody2 = world.CreateStaticBody(position=(33/2,5),shapes=b2PolygonShape(box=(17/2,5)))

body1 = world.CreateDynamicBody(position=(21,10),fixtures=b2FixtureDef(shape=b2PolygonShape(box=(4,0.35)),density=8000,friction=0.2,categoryBits=0x0002,maskBits=0x0004))
body2 = world.CreateDynamicBody(position=(29,10),fixtures=b2FixtureDef(shape=b2PolygonShape(box=(4,0.35)),density=8000,friction=0.2,categoryBits=0x0002,maskBits=0x0004))

n = body1

joint1 = world.CreateRevoluteJoint(bodyA=n,bodyB=groundBody1,anchor=(17,10),collideConnected=False)
joint2 = world.CreateRevoluteJoint(bodyA=groundBody1,bodyB=n,anchor=(17,10),collideConnected=False)

joint3 = world.CreateRevoluteJoint(bodyA=body2,bodyB=body1,anchor=(25,10),collideConnected=False)
joint4 = world.CreateRevoluteJoint(bodyA=body1,bodyB=body2,anchor=(25,10),collideConnected=False)

joint5 = world.CreateRevoluteJoint(bodyA=groundBody2,bodyB=body2,anchor=(33,10),collideConnected=False)
joint6 = world.CreateRevoluteJoint(bodyA=body2,bodyB=groundBody2,anchor=(33,10),collideConnected=False)

box = b2FixtureDef(shape=b2PolygonShape(box=(1,1)),density=10000,friction = 0.3,categoryBits=0x0004,maskBits=0x0002)
box.filter.groupIndex = -2
body = world.CreateDynamicBody(position=(10,20),fixtures=box)

connected = True
timeStep = 1.0/60
vel_iters,pos_iters = 10,10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    Graphics.BackDrop(dif,land,window)


    x1,y1 = joint1.GetReactionForce(1/timeStep)
    x2,y2 = joint2.GetReactionForce(1/timeStep)
    if connected == True:
        x3,y3 = joint3.GetReactionForce(1/timeStep)
        x4,y4 = joint4.GetReactionForce(1/timeStep)
    else:
        x3,x4,y3,y4 = (0,0,0,0)
    x5,y5 = joint5.GetReactionForce(1/timeStep)
    x6,y6 = joint6.GetReactionForce(1/timeStep)

    GB1 = (x1**2+y1**2)**0.5
    B1 = (x3**2+y3**2)**0.5 + (x2**2+y2**2)**0.5
    B2 = (x4**2+y4**2)**0.5 + (x5**2+y5**2)**0.5
    GB2 = (x6**2+y6**2)**0.5

    print(GB1//1000,B1//1000,B2//1000,GB2//1000)

    if B1//1000 > 50000 or B2//1000> 50000:
        world.DestroyJoint(joint3)
        joint3 = None
        world.DestroyJoint(joint4)
        joint4 = None
        connected = False

    x,y = body1.position
    angle = math.pi*2 - body1.angle
    x = 20*x
    y = 600-20*y
    point1 = (x+80*math.cos(angle),y+80*math.sin(angle))
    point2 = (x-80*math.cos(angle),y-80*math.sin(angle))
    pygame.draw.line(window,(100,100,100),point1,point2,7)

    x,y = body2.position
    angle = math.pi*2 - body2.angle
    x = 20*x
    y = 600-20*y
    point1 = (x+ 80*math.cos(angle),y+80*math.sin(angle))
    point2 = (x- 80*math.cos(angle),y-80*math.sin(angle))
    pygame.draw.line(window,(100,100,100),point1,point2,7)

    x,y = body.position
    #print((x,y))
    if y < 11.3  and foo < 1:
        print("###################################################################1")
        foo += 1
    if foo == 1 and y > 11.3:
        print("###################################################################2")
        foo += 1
    if foo ==2 and y < 11.3:
        print("###################################################################3")
        foo += 1

    angle = (2*math.pi)-(body.angle - math.pi/4)
    x = 20*round(x)
    y = 600 - 20*round(y)
    for j in range(0,4):
        point1 = (x+(800**0.5)*(math.cos(angle+(j*math.pi/2))),y+(800**0.5)*(math.sin(angle+(j*math.pi/2))))
        point2 = (x+(800**0.5)*(math.cos(angle+((j+1)*math.pi/2))),y+(800**0.5)*(math.sin(angle+((j+1)*math.pi/2))))
        pygame.draw.line(window,(0,0,0),point1,point2,5)


    world.Step(timeStep,vel_iters,pos_iters)

    world.ClearForces()
    clock.tick()
    print("                         "+str(clock.get_fps()//1))
    pygame.display.update()
    pygame.time.wait(5)



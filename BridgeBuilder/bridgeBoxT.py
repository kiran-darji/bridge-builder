from Box2D import *
import pygame,sys,math
import Graphics

foo = 0

window = pygame.display.set_mode((1000,600),0,32)
clock = pygame.time.Clock()

world = b2World()
dif = "easy"
land = 1


groundBody1 = world.CreateStaticBody(position=(17/2,5),shapes=b2PolygonShape(box=(17/2,5)))
groundBody2 = world.CreateStaticBody(position=(50-17/2,5),shapes=b2PolygonShape(box=(17/2,5)))

body1 = world.CreateDynamicBody(position=(21,10),fixtures=b2FixtureDef(shape=b2PolygonShape(box=(4,0.35)),density=8000,friction=0.2,categoryBits=0x0002,maskBits=0x0004))
body2 = world.CreateDynamicBody(position=(29,10),fixtures=b2FixtureDef(shape=b2PolygonShape(box=(4,0.35)),density=8000,friction=0.2,categoryBits=0x0002,maskBits=0x0004))

fix3 = b2FixtureDef(shape=b2PolygonShape(box=((32**0.5)*0.5,0.35)),density=8000,friction=0.2,categoryBits=0x0002,maskBits=0x0004)
fix3.filter.groupIndex = -2
body3 = world.CreateDynamicBody(position=(19,13),fixtures=fix3,angle=math.pi/4)
fix4 = b2FixtureDef(shape=b2PolygonShape(box=((32**0.5)*0.5,0.35)),density=8000,friction=0.2,categoryBits=0x0002,maskBits=0x0004)
fix4.filter.groupIndex = -2
body4 = world.CreateDynamicBody(position=(23,13),fixtures=fix4,angle=3*math.pi/4)

fix5 = b2FixtureDef(shape=b2PolygonShape(box=((32**0.5)*0.5,0.35)),density=8000,friction=0.2,categoryBits=0x0002,maskBits=0x0004)
fix5.filter.groupIndex = -2
body5 = world.CreateDynamicBody(position=(27,13),fixtures=fix5,angle=math.pi/4)
fix6 = b2FixtureDef(shape=b2PolygonShape(box=((32**0.5)*0.5,0.35)),density=8000,friction=0.2,categoryBits=0x0002,maskBits=0x0004)
fix6.filter.groupIndex = -2
body6 = world.CreateDynamicBody(position=(31,13),fixtures=fix6,angle=3*math.pi/4)

fix7 = b2FixtureDef(shape=b2PolygonShape(box=(4,0.35)),density=8000,friction=0.2,categoryBits=0x0002,maskBits=0x0004)
fix7.filter.groupIndex = -2
body7 = world.CreateDynamicBody(position=(25,16),fixtures=fix7)

joint1 = world.CreateRevoluteJoint(bodyA=body1,bodyB=groundBody1,anchor=(17,10),collideConnected=False)
joint2 = world.CreateRevoluteJoint(bodyA=body3,bodyB=groundBody1,anchor=(17,10),collideConnected=False)

joint3 = world.CreateRevoluteJoint(bodyA=groundBody1,bodyB=body1,anchor=(17,10),collideConnected=False)
joint4 = world.CreateRevoluteJoint(bodyA=body3,bodyB=body1,anchor=(17,10),collideConnected=False)
joint5 = world.CreateRevoluteJoint(bodyA=body4,bodyB=body1,anchor=(25,10),collideConnected=False)
joint6 = world.CreateRevoluteJoint(bodyA=body5,bodyB=body1,anchor=(25,10),collideConnected=False)
joint7 = world.CreateRevoluteJoint(bodyA=body2,bodyB=body1,anchor=(25,10),collideConnected=False)

joint8 = world.CreateRevoluteJoint(bodyA=body1,bodyB=body2,anchor=(25,10),collideConnected=False)
joint9 = world.CreateRevoluteJoint(bodyA=body4,bodyB=body2,anchor=(25,10),collideConnected=False)
joint10 = world.CreateRevoluteJoint(bodyA=body5,bodyB=body2,anchor=(25,10),collideConnected=False)
joint11 = world.CreateRevoluteJoint(bodyA=body6,bodyB=body2,anchor=(33,10),collideConnected=False)
joint12 = world.CreateRevoluteJoint(bodyA=groundBody1,bodyB=body2,anchor=(33,10),collideConnected=False)

joint13 = world.CreateRevoluteJoint(bodyA=groundBody1,bodyB=body3,anchor=(17,10),collideConnected=False)
joint14 = world.CreateRevoluteJoint(bodyA=body1,bodyB=body3,anchor=(17,10),collideConnected=False)
joint15 = world.CreateRevoluteJoint(bodyA=body4,bodyB=body3,anchor=(21,14),collideConnected=False)
joint16 = world.CreateRevoluteJoint(bodyA=body7,bodyB=body3,anchor=(21,14),collideConnected=False)

joint17 = world.CreateRevoluteJoint(bodyA=body1,bodyB=body4,anchor=(25,10),collideConnected=False)
joint18 = world.CreateRevoluteJoint(bodyA=body2,bodyB=body4,anchor=(25,10),collideConnected=False)
joint19 = world.CreateRevoluteJoint(bodyA=body5,bodyB=body4,anchor=(25,10),collideConnected=False)
joint20 = world.CreateRevoluteJoint(bodyA=body3,bodyB=body4,anchor=(21,14),collideConnected=False)
joint21 = world.CreateRevoluteJoint(bodyA=body7,bodyB=body4,anchor=(21,14),collideConnected=False)

joint22 = world.CreateRevoluteJoint(bodyA=body1,bodyB=body5,anchor=(25,10),collideConnected=False)
joint23 = world.CreateRevoluteJoint(bodyA=body2,bodyB=body5,anchor=(25,10),collideConnected=False)
joint24 = world.CreateRevoluteJoint(bodyA=body4,bodyB=body5,anchor=(25,10),collideConnected=False)
joint25 = world.CreateRevoluteJoint(bodyA=body6,bodyB=body5,anchor=(29,14),collideConnected=False)
joint26 = world.CreateRevoluteJoint(bodyA=body7,bodyB=body5,anchor=(29,14),collideConnected=False)

joint27 = world.CreateRevoluteJoint(bodyA=body2,bodyB=body6,anchor=(33,10),collideConnected=False)
joint28 = world.CreateRevoluteJoint(bodyA=body5,bodyB=body6,anchor=(29,14),collideConnected=False)
joint29 = world.CreateRevoluteJoint(bodyA=body7,bodyB=body6,anchor=(29,14),collideConnected=False)
joint30 = world.CreateRevoluteJoint(bodyA=groundBody2,bodyB=body6,anchor=(33,10),collideConnected=False)

joint31 = world.CreateRevoluteJoint(bodyA=body3,bodyB=body7,anchor=(21,14),collideConnected=False)
joint32 = world.CreateRevoluteJoint(bodyA=body4,bodyB=body7,anchor=(21,14),collideConnected=False)
joint33 = world.CreateRevoluteJoint(bodyA=body5,bodyB=body7,anchor=(29,14),collideConnected=False)
joint34 = world.CreateRevoluteJoint(bodyA=body6,bodyB=body7,anchor=(29,14),collideConnected=False)

joint35 = world.CreateRevoluteJoint(bodyA=body2,bodyB=groundBody2,anchor=(33,10),collideConnected=False)
joint36 = world.CreateRevoluteJoint(bodyA=body6,bodyB=groundBody2,anchor=(33,10),collideConnected=False)


box = b2FixtureDef(shape=b2PolygonShape(box=(1,1)),density=10000,friction = 0.3,categoryBits=0x0004,maskBits=0x0002)
box.filter.groupIndex = -2
body = world.CreateDynamicBody(position=(25,20),fixtures=box)


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
    x3,y3 = joint3.GetReactionForce(1/timeStep)
    x4,y4 = joint4.GetReactionForce(1/timeStep)
    x5,y5 = joint5.GetReactionForce(1/timeStep)
    x6,y6 = joint6.GetReactionForce(1/timeStep)
    x7,y7 = joint7.GetReactionForce(1/timeStep)
    x8,y8 = joint8.GetReactionForce(1/timeStep)
    x9,y9 = joint9.GetReactionForce(1/timeStep)
    x10,y10 = joint10.GetReactionForce(1/timeStep)
    x11,y11 = joint11.GetReactionForce(1/timeStep)
    x12,y12 = joint12.GetReactionForce(1/timeStep)  
    x13,y13 = joint13.GetReactionForce(1/timeStep)  
    x14,y14 = joint14.GetReactionForce(1/timeStep)  
    x15,y15 = joint15.GetReactionForce(1/timeStep)  
    x16,y16 = joint16.GetReactionForce(1/timeStep)  
    x17,y17 = joint17.GetReactionForce(1/timeStep)  
    x18,y18 = joint18.GetReactionForce(1/timeStep)  
    x19,y19 = joint19.GetReactionForce(1/timeStep)  
    x20,y20 = joint20.GetReactionForce(1/timeStep)  
    x21,y21 = joint21.GetReactionForce(1/timeStep)  
    x22,y22 = joint22.GetReactionForce(1/timeStep)
    x23,y23 = joint23.GetReactionForce(1/timeStep)
    x24,y24 = joint24.GetReactionForce(1/timeStep)
    x25,y25 = joint25.GetReactionForce(1/timeStep)
    x26,y26 = joint26.GetReactionForce(1/timeStep)
    x27,y27 = joint27.GetReactionForce(1/timeStep)
    x28,y28 = joint28.GetReactionForce(1/timeStep)
    x29,y29 = joint29.GetReactionForce(1/timeStep)
    x30,y30 = joint30.GetReactionForce(1/timeStep)
    x31,y31 = joint31.GetReactionForce(1/timeStep)
    x32,y32 = joint32.GetReactionForce(1/timeStep)
    x33,y33 = joint33.GetReactionForce(1/timeStep)
    x34,y34 = joint34.GetReactionForce(1/timeStep)
    x35,y35 = joint35.GetReactionForce(1/timeStep)
    x36,y36 = joint36.GetReactionForce(1/timeStep)

    GB1 = (x1**2+y1**2)**0.5 + (x2**2+y2**2)**0.5
    B1 = (x3**2+y3**2)**0.5 + (x4**2+y4**2)**0.5 + (x5**2+y5**2)**0.5 + (x6**2+y6**2)**0.5 + (x7**2+y7**2)**0.5
    B2 = (x8**2+y8**2)**0.5 + (x9**2+y9**2)**0.5 + (x10**2+y10**2)**0.5 + (x11**2+y11**2)**0.5 + (x12**2+y12**2)**0.5
    B3 = (x13**2+y13**2)**0.5 + (x14**2+y14**2)**0.5 + (x15**2+y15**2)**0.5 + (x16**2+y16**2)**0.5
    B4 = (x17**2+y17**2)**0.5 + (x18**2+y18**2)**0.5 + (x19**2+y19**2)**0.5 + (x20**2+y20**2)**0.5 + (x21**2+y21**2)**0.5
    B5 = (x22**2+y22**2)**0.5 + (x23**2+y23**2)**0.5 + (x24**2+y24**2)**0.5 + (x25**2+y25**2)**0.5 + (x26**2+y26**2)**0.5
    B6 = (x27**2+y27**2)**0.5 + (x28**2+y28**2)**0.5 + (x29**2+y29**2)**0.5 + (x30**2+y30**2)**0.5
    B7 = (x31**2+y31**2)**0.5 + (x32**2+y32**2)**0.5 + (x33**2+y33**2)**0.5 + (x34**2+y34**2)**0.5
    GB2 = (x35**2+y35**2)**0.5 + (x36**2+y36**2)**0.5

    print(GB1//1000,B1//1000,B2//1000,B3//1000,B4//1000,B5//1000,B6//1000,B7//1000,GB2//1000)

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

    x,y = body3.position
    angle = 2*math.pi -  body3.angle
    x = 20*x
    y = 600-20*y
    point1 = (x+ ((32**0.5)*10)*math.cos(angle),y+80*math.sin(angle))
    point2 = (x- ((32**0.5)*10)*math.cos(angle),y-80*math.sin(angle))
    pygame.draw.line(window,(100,100,100),point1,point2,7)

    x,y = body4.position
    angle = 2*math.pi - body4.angle
    x = 20*x
    y = 600-20*y
    point1 = (x+ ((32**0.5)*10)*math.cos(angle),y+80*math.sin(angle))
    point2 = (x- ((32**0.5)*10)*math.cos(angle),y-80*math.sin(angle))
    pygame.draw.line(window,(100,100,100),point1,point2,7)

    x,y = body5.position
    angle = 2*math.pi - body5.angle
    x = 20*x
    y = 600-20*y
    point1 = (x+ ((32**0.5)*10)*math.cos(angle),y+80*math.sin(angle))
    point2 = (x- ((32**0.5)*10)*math.cos(angle),y-80*math.sin(angle))
    pygame.draw.line(window,(100,100,100),point1,point2,7)

    x,y = body6.position
    angle = 2*math.pi - body6.angle
    x = 20*x
    y = 600-20*y
    point1 = (x+ ((32**0.5)*10)*math.cos(angle),y+80*math.sin(angle))
    point2 = (x- ((32**0.5)*10)*math.cos(angle),y-80*math.sin(angle))
    pygame.draw.line(window,(100,100,100),point1,point2,7)

    x,y = body7.position
    angle = math.pi*2 - body7.angle
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


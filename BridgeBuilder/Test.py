from Box2D import *
import pygame,sys,math,Graphics,Classes,Build

def createJoints(joint,world,groundBody1,groundBody2):
    for materialA in joint['materials']:
        for materialB in joint['materials']:
            if materialA != materialB:

                if materialA.getMaterial() == "Rope" or materialA.getMaterial()== "Cable":
                    if joint['index'] == materialA.getJoint1():
                        bodyA = materialA.getBody()[0]
                    elif joint['index'] == materialA.getJoint2():
                        bodyA = materialA.getBody()[-1]
                else:
                    bodyA = materialA.getBody()
    
                if materialB.getMaterial() == "Rope" or materialB.getMaterial()== "Cable":
                    if joint['index'] == materialB.getJoint1():
                        bodyB = materialB.getBody()[0]
                    elif joint['index'] == materialB.getJoint2():
                        bodyB = materialB.getBody()[-1]
                else:
                    bodyB = materialB.getBody()

                Joint = world.CreateRevoluteJoint(bodyA=bodyA,bodyB=bodyB,anchor=joint['point'],collideConnected=False)
                if joint['index'] == materialB.getJoint1():
                    materialB.addB2joints1({"reference":Joint,"maxForce":materialA.getMaxForce()})
                elif joint['index'] == materialB.getJoint2():
                    materialB.addB2joints2({"reference":Joint,"maxForce":materialA.getMaxForce()})


    if joint['onGround1']:
        bodyA = groundBody1
    elif joint['onGround2']:
        bodyA = groundBody2

    if joint['onGround1'] or joint['onGround2']:
        for material in joint['materials']:
            if material.getMaterial() == "Rope" or material.getMaterial()== "Cable":
                if joint['index'] == material.getJoint1():
                    bodyB = material.getBody()[0]
                elif joint['index'] == material.getJoint2():
                    bodyB = material.getBody()[-1]
            else:
                bodyB = material.getBody()

            Joint = world.CreateRevoluteJoint(bodyA=bodyA,bodyB=bodyB,anchor=joint['point'],collideConnected=False)
            
            if joint['index'] == material.getJoint1():
                material.addB2joints1({"reference":Joint,"maxForce":material.getMaxForce()})
            elif joint['index'] == material.getJoint2():
                material.addB2joints2({"reference":Joint,"maxForce":material.getMaxForce()})


def loadBridge(bridgeID,world):
    materialStack,jointList,jointNum,dif,land = Build.loadBridge(bridgeID)
    Dirt1Y,Dirt1width,Dirt1height,Dirt2X,Dirt2Y,Dirt2width,Dirt2height = Graphics.dirtSize(dif,land)

    Dirt1Y = 30 - Dirt1Y/20
    Dirt1width = Dirt1width/20
    Dirt1height = Dirt1height/20
    Dirt2X = Dirt2X/20
    Dirt2Y = 30 - Dirt2Y/20
    Dirt2width = Dirt2width/20
    Dirt2height = Dirt2height/20

    for joint in jointList:
        convx,convy = joint['point']
        joint['point'] = (convx/20,30-convy/20)

    GB1fix = b2FixtureDef(shape=b2PolygonShape(box=(Dirt1width/2,Dirt1height/2)),friction=0.2,categoryBits=0x0002,maskBits=0x0004)
    groundBody1 = world.CreateStaticBody(position=(Dirt1width/2,Dirt1height/2),fixtures = GB1fix)

    GB2fix = b2FixtureDef(shape=b2PolygonShape(box=(Dirt2width/2,Dirt2height/2)),friction=0.2,categoryBits=0x0002,maskBits=0x0004)
    groundBody2 = world.CreateStaticBody(position=(50-Dirt2width/2,Dirt2height/2),fixtures = GB2fix)

    wallfix = b2FixtureDef(shape=b2PolygonShape(box=(1,15)),friction=0.2,categoryBits=0x0002,maskBits=0x0004)
    wall1 = world.CreateStaticBody(position=(-1,15),fixtures = wallfix)
    wall2 = world.CreateStaticBody(position=(51,15),fixtures = wallfix)

    for material in materialStack:
        material.createBody(world)

    for joint in jointList:
        materialAboutJoint = []
        for material in materialStack:
            if joint['index'] == material.getJoint1() or joint['index'] == material.getJoint2():
                materialAboutJoint.append(material)
            joint['materials'] = materialAboutJoint
        jointx,jointy = joint['point']

        if (jointx == Dirt1width and jointy <= Dirt1Y) or (jointx <= Dirt1width and jointy == Dirt1Y):
            joint['onGround1'] = True
            joint['onGround2'] = False
        elif (jointx == Dirt2X and jointy <= Dirt2Y) or (jointx >= Dirt2X and jointy == Dirt2Y):
            joint['onGround1'] = False
            joint['onGround2'] = True
        else:
            joint['onGround1'] = False
            joint['onGround2'] = False
        
        createJoints(joint,world,groundBody1,groundBody2)

    return (materialStack,jointList,dif,land)

def Main(info,window):
    world = b2World()
    materialStack,jointList,dif,land = loadBridge(info['bridgeID'],world)
    clock = pygame.time.Clock()
    timeStep = 1.0/25
    vel_iters,pos_iters = 7,7
    frameCount = 0

    font = pygame.font.SysFont(None,90)
    text1 = font.render('Loading', True,(255,255,255),None)
    text1Rect = text1.get_rect()
    text1Rect.centerx = window.get_rect().centerx
    text1Rect.centery = window.get_rect().centery
    text2 = font.render('Loading', True,(0,0,0),None)
    text2Rect = text2.get_rect()
    text2Rect.centerx = window.get_rect().centerx - 5
    text2Rect.centery = window.get_rect().centery - 5

    buttons = {
    'quit':Classes.Button('        Quit         ',150,50),
    'edit':Classes.Button('        Edit         ',400,50)
}

    if info['vehicle'] == "car":
        vehicle = Classes.car()
    elif info['vehicle'] == "bike":
        vehicle = Classes.bike()
    elif info['vehicle'] == "truck":
        vehicle = Classes.truck()

    if land == 1:
        height = 10
    elif land == 2:
        height = 13
    elif land == 3:
        height = 8

    vehicle.create(world,height)

    forward,back,click = False,False,False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True
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

        frameCount += 1

        if frameCount%5 == 0 and frameCount > 100:
            for material in materialStack:
                material.ifBreak(world,timeStep)
    
        Graphics.BackDrop(dif,land,window)

        for material in materialStack:
            material.testDraw(window)
    
        vehicle.Draw(window)

        if frameCount > 100:
            if forward:
                vehicle.forward()
            elif back:
                vehicle.back()
            elif (forward == False and back != True) or (back == False and forward != True):
                vehicle.stop()
        else:   
            window.blit(text2,text2Rect)
            window.blit(text1,text1Rect)

        buttons['quit'].create(window)
        buttons['edit'].create(window)

        if click:
            if buttons['quit'].ifClick():
                info['test'] = False
                info2 = ["sec",info]
                return info2
            elif buttons['edit'].ifClick():
                info['test'] = False
                info['loadBridge'] = True
                info['build'] = True
                info2 = ["build",info]
                return info2


        world.Step(timeStep,vel_iters,pos_iters)

        world.ClearForces()

        #clock.tick()
        #print(clock.get_fps())

        pygame.display.update()
        pygame.time.wait(5)

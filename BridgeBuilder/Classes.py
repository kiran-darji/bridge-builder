from Box2D import *
import pygame
import Graphics
import math
WHITE = (255,255,255)
LBROWN = (204,102,0)
DBROWN = (51,0,0)


class TextBox():
    def __init__(self,cap,height,width,center,colour1=LBROWN,colour2=DBROWN):
        self.cap = cap
        self.height = height
        self.width = width
        self.center = center
        self.colour1 = colour1
        self.colour2 = colour2

    def create(self,window):
        word = self.cap
        font = pygame.font.SysFont(None,50)
        height = self.height / 2
        width = self.width / 2
        x,y  = self.center
        
        if type(word) == str:
            temp  = word
            word = []
            word.append(temp)
        
        poly1 = ((x-width,y+(height-5)),(x-(width-5),y+height),(x+(width-5),y+height),(x+width,y+(height-5)),(x+width,y-(height-5)),(x+(width-5),y-height),(x-(width-5),y-height),(x-width,y-(height-5)))
        poly2 = ((x-(width+5),y+(height-10)),(x-width,y+(height-5)),(x+(width-10),y+(height-5)),(x+(width-5),y+(height-10)),(x+(width-5),y-height),(x+(width-10),y-(height+5)),(x-width,y-(height+5)),(x-(width+5),y-height))

        pygame.draw.polygon(window,self.colour2,poly2)
        pygame.draw.polygon(window,self.colour1,poly1)


        if (len(word))%2 == 0:
            start = 25+((-50)*(len(word)/2))
            end = abs(start)+25
        else:
            start = (-50)*((len(word)-1)/2)
            end = abs(start)+50

        wordTrack = 0
        for loc in range(int(start), int(end), 50):
            Text = font.render(word[wordTrack],True,WHITE,None)
            textRect = Text.get_rect()

            textRect.centerx = x
            textRect.centery = y + loc

            window.blit(Text,textRect)
            wordTrack += 1

class InputBox():
    def __init__(self,name,xCo,yCo,width,height):
        self.name = name
        self.cap = ""
        self.yCo = yCo
        self.xCo = xCo
        self.rect = pygame.Rect(xCo,yCo,width,height)
        self.active = False

    def create(self,window):
        font = pygame.font.SysFont(None, 50)
        xCo = self.xCo
        yCo = self.yCo

        text1 = font.render(self.cap,True,WHITE,None)
        textRect1 = text1.get_rect()
        text2 = font.render(self.name,True,WHITE,None)
        textRect2 = text2.get_rect()

        textRect1.left = xCo + 10
        textRect1.top = yCo + 10
        textRect2.right = self.rect.left - 10
        textRect2.top = self.rect.top + 10

        if self.active:
            colour = LBROWN
        else:
            colour = DBROWN

        pygame.draw.rect(window,colour,self.rect)

        window.blit(text1,textRect1)
        window.blit(text2,textRect2)

    def ifClick(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) == True:
            return True
        else:
            return False
    
    def Add(self, char):
        self.cap += char

    def makeActive(self):
        self.active = True

    def deActive(self):
        self.active = False

    def getActive(self):
        active = self.active
        return active

    def Back(self):
        self.cap = self.cap[:-1]

    def getCapLength(self):
        length = len(self.cap)
        return length

    def getCap(self):
        cap = self.cap
        return cap

class Button():
    def __init__(self,cap,locx,locy,colour1=LBROWN,colour2=DBROWN,width=105,height=20):
        self.cap = cap
        self.locy = locy
        self.locx = locx
        self.rect = 0
        self.colour1 = colour1
        self.colour2 = colour2
        self.width = width
        self.height = height

    def create(self,window,error=False):
        word = self.cap
        font = pygame.font.SysFont(None, 50)
        locy = self.locy
        locx = self.locx
        width = self.width
        height = self.height

        text = font.render(word,True,WHITE,None)
        textRect = text.get_rect()
        self.rect = text.get_rect()

        textRect.centerx = locx
        textRect.centery = locy
        self.rect.centerx = locx
        self.rect.centery = locy

        x = textRect.centerx
        y = textRect.centery
        poly1 = ((x-(width+5),y+height),(x-width,y+height+5),(x+width,y+height+5),(x+width+5,y+height),(x+width+5,y-height),(x+width,y-(height+5)),(x-width,y-(height+5)),(x-(width+5),y-height))

        poly2 = ((x-(width+10),y+height-5),(x-(width+5),y+height),(x+width-5,y+height),(x+width,y+height-5),(x+width,y-(height+5)),(x+width-5,y-(height+10)),(x-(width+5),y-(height+10)),(x-(width+10),y-(height+5)))

        if textRect.collidepoint(pygame.mouse.get_pos()) and error == False:
            pygame.draw.polygon(window,self.colour1,poly2)
            pygame.draw.polygon(window,self.colour2,poly1)
        else:
            pygame.draw.polygon(window,self.colour2,poly2)
            pygame.draw.polygon(window,self.colour1,poly1)

        window.blit(text,textRect)

    def ifClick(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) == True:
            return True
        else:
            return False


class stickButton(Button):
    def __init__(self,cap,locx,locy,colour1=LBROWN,colour2=DBROWN):
        Button.__init__(self,cap,locx,locy,colour1,colour2)
        self.On = False

    def create(self,window):
        word = self.cap
        font = pygame.font.SysFont(None, 50)
        locy = self.locy
        locx = self.locx

        text = font.render(word,True,WHITE,None)
        textRect = text.get_rect()
        self.rect = text.get_rect()

        textRect.centerx = locx
        textRect.centery = locy
        self.rect.centerx = locx
        self.rect.centery = locy

        x = textRect.centerx
        y = textRect.centery
        poly1 = ((x-80,y+20),(x-75,y+25),(x+75,y+25),(x+80,y+20),(x+80,y-20),(x+75,y-25),(x-75,y-25),(x-80,y-20))
        poly2 = ((x-85,y+15),(x-80,y+20),(x+70,y+20),(x+75,y+15),(x+75,y-25),(x+70,y-30),(x-80,y-30),(x-85,y-25))

        if self.On:
            pygame.draw.polygon(window,self.colour1,poly2)
            pygame.draw.polygon(window,self.colour2,poly1)
        else:
            pygame.draw.polygon(window,self.colour2,poly2)
            pygame.draw.polygon(window,self.colour1,poly1)

        window.blit(text,textRect)


    def ifClick(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) == True:
            return True
        else:
            return False
    
    def getOn(self):
        ifOn = self.On
        return ifOn

    def turnOn(self):
        self.On = True
    def turnOff(self):
        self.On = False

class Material():
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        self.joint1 = 0
        self.joint2 = 0
        self.Colour = 0
        self.error = False
        self.material = ""
        self.body = ""
        self.groupIndex = -2
        self.density = 1
        self.B2joints1 = []
        self.B2joints2 = []
        self.maxForce = 0

    def getMaxForce(self):
        maxForce = self.maxForce
        return maxForce

    def ifBreak(self,world,timeStep):
        totalX = 0
        totalY = 0
        numOfMaterials = len(self.B2joints1) + len(self.B2joints2)
        maxForce = 0
        for joint in self.B2joints1:
            x,y = joint['reference'].GetReactionForce(1/timeStep)
            totalX += x
            totalY += y
            maxForce += joint['maxForce']
        reaction1 = (totalX**2 + totalY**2)**0.5
    
        totalX = 0
        totalY = 0
        for joint in self.B2joints2:
            x,y = joint['reference'].GetReactionForce(1/timeStep)
            totalX += x
            totalY += y
            maxForce += joint['maxForce']
        reaction2 = (totalX**2 + totalY**2)**0.5
    
        maxForce = (maxForce + self.maxForce) / (numOfMaterials + 1)

        if reaction1 + reaction2 > maxForce:
            if reaction1 > reaction2:
                for joint in self.B2joints1:
                    world.DestroyJoint(joint['reference'])
                del self.B2joints1[:]
            else:
                for joint in self.B2joints2:
                    world.DestroyJoint(joint['reference'])
                del self.B2joints2[:]

    def addB2joints2(self,joint):
        self.B2joints2.append(joint)

    def addB2joints1(self,joint):
        self.B2joints1.append(joint)

    def getBody(self):
        body = self.body
        return body  

    def getMaterial(self):
        material = self.material
        return material

    def errorTrue(self):
        self.error = True
    
    def getJoint1(self):
        joint = self.joint1
        return joint
    
    def getJoint2(self):
        joint = self.joint2
        return joint

    def getError(self):
        error = self.error
        return error

    def getStart(self):
        pos = (self.x1,self.y1)
        return pos
    
    def getEnd(self):
        pos = (self.x2,self.y2)
        return pos

    def setjoint1(self,n):
        self.joint1 = n

    def setjoint2(self,n):
        self.joint2 = n

    def checkPlacement(self):
        if ((self.x1 == self.x2) and (self.y1 == self.y2)) or (((((self.x2-self.x1)**2)+((self.y2-self.y1)**2))**0.5)>200):
            self.error = True
        else:
            self.error = False

    def setCo1(self,x,y):
        self.x1 = x
        self.y1 = y
    
    def setCo2(self,x,y):
        self.x2 = x
        self.y2 = y

    def updateLocation(self,x,y):
        self.x2 = x
        self.y2 = y

    def Draw(self,window):
        pygame.draw.line(window,(0,0,0),(self.x1,self.y1),(self.x2,self.y2),11)
        if self.error == False:
            pygame.draw.line(window,self.Colour,(self.x1,self.y1),(self.x2,self.y2),7)
        else:
            pygame.draw.line(window,(233,12,12),(self.x1,self.y1),(self.x2,self.y2),7)


    def createBody(self,world):
        x1 = self.x1 / 20
        x2 = self.x2 / 20
        y1 = 30 - self.y1/20
        y2 = 30 - self.y2/20
        deltax = x2 - x1
        deltay = y2 - y1
        length = (deltay**2 + deltax**2)**0.5
        angle = math.atan2(deltay,deltax)

        pos = (x1+deltax/2,y1+deltay/2)

        fix = b2FixtureDef(shape=b2PolygonShape(box=(length/2,0.2)),density=self.density,friction=0.2,categoryBits=0x0002,maskBits=0x0004)
        fix.filter.groupIndex = self.groupIndex
        
        self.body = world.CreateDynamicBody(position=pos,fixtures=fix,angle=angle)

    def testDraw(self,window):
        posX,posY = self.body.position
        posX *= 20
        posY = 600 - posY*20
        angle = 2*math.pi - self.body.angle
    
        radius = (((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5)/2
        
        self.x1 = posX - radius*math.cos(angle)
        self.y1 = posY - radius*math.sin(angle)
        self.x2 = posX + radius*math.cos(angle)
        self.y2 = posY + radius*math.sin(angle)
        
        self.Draw(window)


class Steel(Material):
    def __init__(self):
        Material.__init__(self)
        self.Colour = (224,223,219)
        self.material = "Steel"
        self.density = 8000
        self.maxForce = 4000000

class Wood(Material):
    def __init__(self):
        Material.__init__(self)
        self.Colour = (120,81,45)
        self.material = "Wood"
        self.density = 2000
        self.maxForce = 3000000

class Road(Material):
    def __init__(self):
        Material.__init__(self)
        self.Colour = (0,0,0)
        self.material = "Road"
        self.groupIndex = 1
        self.density = 3000
        self.maxForce = 2000000

class Rope(Material):
    def __init__(self):
        Material.__init__(self)
        self.Colour = (120,81,45)
        self.material = "Rope"
        self.density = 500
        self.body = []
        self.chainJoints = []
        self.maxForce = 2000000

    def ifBreak(self,world,timeStep):
        Material.ifBreak(self,world,timeStep)
        toDelete = -1
        for joint in range(0,len(self.chainJoints)):
            forceX,forceY = self.chainJoints[joint].GetReactionForce(1/timeStep)
            force = (forceX**2 + forceY**2)**0.5
            if force > self.maxForce:
                toDelete = joint
        if toDelete != -1:
            world.DestroyJoint(self.chainJoints[toDelete])
            del self.chainJoints[toDelete]
            

    def checkPlacement(self):
        if ((self.x1 == self.x2) and (self.y1 == self.y2)) or (((((self.x2-self.x1)**2)+((self.y2-self.y1)**2))**0.5)>400):
            self.error = True
        else:
            self.error = False
    
    def Draw(self,window):
        xChange = self.x2 - self.x1
        yChange = self.y2 - self.y1
    
        for i in range(0,10):
            xPoint1 = self.x1 + (i*0.1*xChange)
            yPoint1 = self.y1 + (i*0.1*yChange)
            xPoint2 = xPoint1 + (0.06*xChange)
            yPoint2 = yPoint1 + (0.06*yChange)

            pygame.draw.line(window,(0,0,0),(xPoint1,yPoint1),(xPoint2,yPoint2),11)
            if self.error == False:
                pygame.draw.line(window,self.Colour,(xPoint1,yPoint1),(xPoint2,yPoint2),7)
            else:
                pygame.draw.line(window,(233,12,12),(xPoint1,yPoint1),(xPoint2,yPoint2),7)


    def createBody(self,world):
        x1 = self.x1 / 20
        x2 = self.x2 / 20
        y1 = 30 - self.y1/20
        y2 = 30 - self.y2/20
        deltax = x2 - x1
        deltay = y2 - y1
        length = (deltay**2 + deltax**2)**0.5
        angle = math.atan2(deltay,deltax)

        stepx = deltax/10
        stepy = deltay/10

        fix = b2FixtureDef(shape=b2PolygonShape(box=(length/20,0.35)),density=self.density,friction=0.2,categoryBits=0x0002,maskBits=0x0004)
        fix.filter.groupIndex = self.groupIndex
            
        prevBody = ""
        
        for i in range(0,10):
            pos = (x1 + (i+0.5)*stepx, y1 + (i+0.5)*stepy)
            body = world.CreateDynamicBody(position=pos,fixtures = fix,angle = angle)
            if i != 0:
                joint = world.CreateRevoluteJoint(bodyA=prevBody,bodyB=body,anchor=(x1 + i*stepx, y1 + i*stepy))
                self.chainJoints.append(joint)
            self.body.append(body)

            prevBody = body

    
    def testDraw(self,window):
        radius = (((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5)/20

        for body in self.body:
            posX,posY = body.position
            posX *= 20
            posY = 600 - posY*20
            angle = 2*math.pi - body.angle

            point1 = (posX - radius*math.cos(angle),posY - radius*math.sin(angle))
            point2 = (posX + radius*math.cos(angle),posY + radius*math.sin(angle))

            pygame.draw.line(window,(0,0,0),point1,point2,11)
            pygame.draw.line(window,self.Colour,point1,point2,7)


class Cable(Material):
    def __init__(self):
        Material.__init__(self)
        self.Colour = (224,223,219)
        self.material = "Cable"
        self.density = 1500
        self.body = []
        self.chainJoints = []
        self.maxForce = 3000000

    def ifBreak(self,world,timeStep):
        Material.ifBreak(self,world,timeStep)
        toDelete = -1
        for joint in range(0,len(self.chainJoints)):
            forceX,forceY = self.chainJoints[joint].GetReactionForce(1/timeStep)
            force = (forceX**2 + forceY**2)**0.5
            if force > self.maxForce:
                toDelete = joint
        if toDelete != -1:
            world.DestroyJoint(self.chainJoints[toDelete])
            del self.chainJoints[toDelete]

    def checkPlacement(self):
        if ((self.x1 == self.x2) and (self.y1 == self.y2)) or (((((self.x2-self.x1)**2)+((self.y2-self.y1)**2))**0.5)>400):
            self.error = True
        else:
            self.error = False

    def Draw(self,window):
        xChange = self.x2 - self.x1
        yChange = self.y2 - self.y1

        for i in range(0,10):
            xPoint1 = self.x1 + (i*0.1*xChange)
            yPoint1 = self.y1 + (i*0.1*yChange)
            xPoint2 = xPoint1 + (0.06*xChange)
            yPoint2 = yPoint1 + (0.06*yChange)

            pygame.draw.line(window,(0,0,0),(xPoint1,yPoint1),(xPoint2,yPoint2),11)
            if self.error == False:
                pygame.draw.line(window,self.Colour,(xPoint1,yPoint1),(xPoint2,yPoint2),7)
            else:
                pygame.draw.line(window,(233,12,12),(xPoint1,yPoint1),(xPoint2,yPoint2),7)


    def createBody(self,world):
        x1 = self.x1 / 20
        x2 = self.x2 / 20
        y1 = 30 - self.y1/20
        y2 = 30 - self.y2/20
        deltax = x2 - x1
        deltay = y2 - y1
        length = (deltay**2 + deltax**2)**0.5
        angle = math.atan2(deltay,deltax)

        stepx = deltax/10
        stepy = deltay/10

        fix = b2FixtureDef(shape=b2PolygonShape(box=(length/20,0.35)),density=self.density,friction=0.2,categoryBits=0x0002,maskBits=0x0004)
        fix.filter.groupIndex = self.groupIndex

        prevBody = ""

        for i in range(0,10):
            pos = (x1 + (i+0.5)*stepx, y1 + (i+0.5)*stepy)
            body = world.CreateDynamicBody(position=pos,fixtures = fix,angle = angle)
            if i != 0:
                joint = world.CreateRevoluteJoint(bodyA=prevBody,bodyB=body,anchor=(x1 + i*stepx, y1 + i*stepy))
                self.chainJoints.append(joint)
            self.body.append(body)

            prevBody = body


    def testDraw(self,window):
        radius = (((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5)/20

        for body in self.body:
            posX,posY = body.position
            posX *= 20
            posY = 600 - posY*20
            angle = 2*math.pi - body.angle

            point1 = (posX - radius*math.cos(angle),posY - radius*math.sin(angle))
            point2 = (posX + radius*math.cos(angle),posY + radius*math.sin(angle))

            pygame.draw.line(window,(0,0,0),point1,point2,11)
            pygame.draw.line(window,self.Colour,point1,point2,7)




class vehicle():
    def __init__(self):
        self.chassis = ""
        self.wheel1 = ""
        self.wheel2 = ""
        self.joint1 = ""
        self.joint2 = ""

    def forward(self):
        self.joint1.motorSpeed = -30
        self.joint2.motorSpeed = -30

    def back(self):
        self.joint1.motorSpeed = 30
        self.joint2.motorSpeed = 30
    
    def stop(self):
        self.joint1.motorSpeed = 0
        self.joint2.motorSpeed = 0

class car(vehicle):
    def create(self,world,height):
        height += 3
    
        chassisDef = b2FixtureDef(shape=b2PolygonShape(box=(1.5,0.8)),density=500,friction=0.3,categoryBits=0x0004,maskBits=0x0002)
        chassisDef.filter.groupIndex = -2
        self.chassis = world.CreateDynamicBody(position=(4,height),fixtures=chassisDef)

        wheel1Def = b2FixtureDef(shape=b2CircleShape(radius=0.8),density=100,categoryBits=0x0004,maskBits=0x0002)
        wheel1Def.filter.groupIndex = -2
        self.wheel1 = world.CreateDynamicBody(position=(5.5,height-0.8),fixtures=wheel1Def)

        wheel2Def = b2FixtureDef(shape=b2CircleShape(radius=0.8),density=100,categoryBits=0x0004,maskBits=0x0002)
        wheel2Def.filter.groupIndex = -2
        self.wheel2 = world.CreateDynamicBody(position=(2.5,height-0.8),fixtures=wheel2Def)

        self.joint1 = world.CreateWheelJoint(bodyA=self.chassis,bodyB=self.wheel1,anchor=(5.5,height-0.8),axis=(0,1),motorSpeed=0.0,maxMotorTorque=5000.0,enableMotor=True,frequencyHz=20.0,dampingRatio=0.5,collideConnected=False)

        self.joint2 = world.CreateWheelJoint(bodyA=self.chassis,bodyB=self.wheel2,anchor=(2.5,height-0.8),axis=(0,1),motorSpeed=0.0,maxMotorTorque=5000.0,enableMotor=True,frequencyHz=20.0,dampingRatio=0.5,collideConnected=False)


    def Draw(self,window):
        angle = 2*math.pi- self.chassis.angle

        x1,y1 = self.wheel1.position
        x1 = int(x1*20)
        y1 = int(600-y1*20)
        point3 = (x1+32*math.sin(angle),y1-32*math.cos(angle))
        point4 = (x1,y1)

        x2,y2 = self.wheel2.position
        x2 = int(x2*20)
        y2 = int(600-y2*20)
        point2 = (x2+32*math.sin(angle),y2-32*math.cos(angle))
        point1 = (x2,y2)

        pygame.draw.line(window,(0,0,0),point1,point2,5)
        pygame.draw.line(window,(0,0,0),point2,point3,5)
        pygame.draw.line(window,(0,0,0),point3,point4,5)
        pygame.draw.line(window,(0,0,0),point4,point1,5)
        pygame.draw.circle(window,(0,0,0),(x1,y1),16,5)
        pygame.draw.circle(window,(0,0,0),(x2,y2),16,5)


class bike(vehicle):
    def create(self,world,height):
        height += 3

        chassisDef = b2FixtureDef(shape=b2PolygonShape(box=(1.5,0.5)),density=500,friction=0.3,categoryBits=0x0004,maskBits=0x0002)
        chassisDef.filter.groupIndex = -2
        self.chassis = world.CreateDynamicBody(position=(4,height),fixtures=chassisDef)

        wheel1Def = b2FixtureDef(shape=b2CircleShape(radius=0.8),density=100,categoryBits=0x0004,maskBits=0x0002)
        wheel1Def.filter.groupIndex = -2
        self.wheel1 = world.CreateDynamicBody(position=(5.5,height-0.5),fixtures=wheel1Def)

        wheel2Def = b2FixtureDef(shape=b2CircleShape(radius=0.8),density=100,categoryBits=0x0004,maskBits=0x0002)
        wheel2Def.filter.groupIndex = -2
        self.wheel2 = world.CreateDynamicBody(position=(2.5,height-0.5),fixtures=wheel2Def)

        self.joint1 = world.CreateWheelJoint(bodyA=self.chassis,bodyB=self.wheel1,anchor=(5.5,height-0.5),axis=(0,1),motorSpeed=0.0,maxMotorTorque=5000.0,enableMotor=True,frequencyHz=20.0,dampingRatio=0.5,collideConnected=False)

        self.joint2 = world.CreateWheelJoint(bodyA=self.chassis,bodyB=self.wheel2,anchor=(2.5,height-0.5),axis=(0,1),motorSpeed=0.0,maxMotorTorque=5000.0,enableMotor=True,frequencyHz=20.0,dampingRatio=0.5,collideConnected=False)


    def Draw(self,window):
        angle = 2*math.pi- self.chassis.angle

        x1,y1 = self.wheel1.position
        x1 = int(x1*20)
        y1 = int(600-y1*20)
        point3 = (x1+20*math.sin(angle),y1-20*math.cos(angle))
        point4 = (x1,y1)

        x2,y2 = self.wheel2.position
        x2 = int(x2*20)
        y2 = int(600-y2*20)
        point2 = (x2+20*math.sin(angle),y2-20*math.cos(angle))
        point1 = (x2,y2)

        pygame.draw.line(window,(0,0,0),point1,point2,5)
        pygame.draw.line(window,(0,0,0),point2,point3,5)
        pygame.draw.line(window,(0,0,0),point3,point4,5)
        pygame.draw.line(window,(0,0,0),point4,point1,5)
        pygame.draw.circle(window,(0,0,0),(x1,y1),16,5)
        pygame.draw.circle(window,(0,0,0),(x2,y2),16,5)


class truck(vehicle):
    def create(self,world,height):
        height += 3

        chassisDef = b2FixtureDef(shape=b2PolygonShape(box=(2.5,1)),density=500,friction=0.3,categoryBits=0x0004,maskBits=0x0002)
        chassisDef.filter.groupIndex = -2
        self.chassis = world.CreateDynamicBody(position=(4,height),fixtures=chassisDef)

        wheel1Def = b2FixtureDef(shape=b2CircleShape(radius=0.8),density=100,categoryBits=0x0004,maskBits=0x0002)
        wheel1Def.filter.groupIndex = -2
        self.wheel1 = world.CreateDynamicBody(position=(6.5,height-1),fixtures=wheel1Def)

        wheel2Def = b2FixtureDef(shape=b2CircleShape(radius=0.8),density=100,categoryBits=0x0004,maskBits=0x0002)
        wheel2Def.filter.groupIndex = -2
        self.wheel2 = world.CreateDynamicBody(position=(1.5,height-1),fixtures=wheel2Def)

        self.joint1 = world.CreateWheelJoint(bodyA=self.chassis,bodyB=self.wheel1,anchor=(6.5,height-1),axis=(0,1),motorSpeed=0.0,maxMotorTorque=5000.0,enableMotor=True,frequencyHz=20.0,dampingRatio=0.5,collideConnected=False)

        self.joint2 = world.CreateWheelJoint(bodyA=self.chassis,bodyB=self.wheel2,anchor=(1.5,height-1),axis=(0,1),motorSpeed=0.0,maxMotorTorque=5000.0,enableMotor=True,frequencyHz=20.0,dampingRatio=0.5,collideConnected=False)


    def Draw(self,window):
        angle = 2*math.pi- self.chassis.angle

        x1,y1 = self.wheel1.position
        x1 = int(x1*20)
        y1 = int(600-y1*20)
        point3 = (x1+40*math.sin(angle),y1-40*math.cos(angle))
        point4 = (x1,y1)

        x2,y2 = self.wheel2.position
        x2 = int(x2*20)
        y2 = int(600-y2*20)
        point2 = (x2+40*math.sin(angle),y2-40*math.cos(angle))
        point1 = (x2,y2)

        pygame.draw.line(window,(0,0,0),point1,point2,5)
        pygame.draw.line(window,(0,0,0),point2,point3,5)
        pygame.draw.line(window,(0,0,0),point3,point4,5)
        pygame.draw.line(window,(0,0,0),point4,point1,5)
        pygame.draw.circle(window,(0,0,0),(x1,y1),16,5)
        pygame.draw.circle(window,(0,0,0),(x2,y2),16,5)

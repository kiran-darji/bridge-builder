import pygame
import math

White = (255,255,255)
Black = (0,0,0)
DirtBrown = (97,63,16)
GrassGreen = (44,176,55)
CloudWhite = (250,242,248)
oceanBlue = (79,66,181)
skyBlue = (135,206,235)
DarkBrown = (51,0,0)
LightBrown = (204,102,0)


def generateOct(window,x,y):
    poly1 = ((x-110,y+105),(x-105,y+110),(x+105,y+110),(x+110,y+105),(x+110,y-105),(x+105,y-110),(x-105,y-110),(x-110,y-105))
    poly2 = ((x-115,y+100),(x-110,y+105),(x+100,y+105),(x+105,y+100),(x+105,y-110),(x+100,y-115),(x-110,y-115),(x-115,y-110))
    poly3 = ((x-95,y+90),(x-90,y+95),(x+90,y+95),(x+95,y+90),(x+95,y-90),(x+90,y-95),(x-90,y-95),(x-95,y-90))

    pygame.draw.polygon(window,DarkBrown,poly2)
    pygame.draw.polygon(window,LightBrown,poly1)
    pygame.draw.polygon(window,skyBlue,poly3)


def LandImage(window):
    centerY = 300
    var = 20
    for centerX in range(250,1000,250):
        generateOct(window,centerX,centerY)
        poly1 = ((centerX-90,centerY+95),(centerX-95,centerY+90),(centerX-95,centerY-var),(centerX-35,centerY-var),(centerX-35,centerY+95))
        poly2 = ((centerX+90,centerY+95),(centerX+95,centerY+90),(centerX+95,centerY+var),(centerX+35,centerY+var),(centerX+35,centerY+95))
        pygame.draw.polygon(window,DirtBrown,poly1)
        pygame.draw.polygon(window,DirtBrown,poly2)
        pygame.draw.rect(window,GrassGreen,(centerX-95,centerY-var,61,10))
        pygame.draw.rect(window,GrassGreen,(centerX+35,centerY+var,61,10))
        var -= 20


def DifImage(window,op):
    if op == 1:
        yvar = 0
    elif op == 2:
        yvar = -20
    elif op == 3:
        yvar = 20

    yloc = 300
    xvar = 15
    width = 81
    for xloc in range(250,1000,250):
        generateOct(window,xloc,yloc)
        poly1 = ((xloc-90,yloc+95),(xloc-95,yloc+90),(xloc-95,yloc+yvar),(xloc-xvar,yloc+yvar),(xloc-xvar,yloc+95))
        poly2 = ((xloc+90,yloc+95),(xloc+95,yloc+90),(xloc+95,yloc-yvar),(xloc+xvar,yloc-yvar),(xloc+xvar,yloc+95))
        pygame.draw.polygon(window,DirtBrown,poly1)
        pygame.draw.polygon(window,DirtBrown,poly2)
        pygame.draw.rect(window,GrassGreen,(xloc-95,yloc+yvar,width,10))
        pygame.draw.rect(window,GrassGreen,(xloc+xvar,yloc-yvar,width,10))
        xvar += 20
        width -= 20

def vehicleImage(window):
    for xloc in range(250,1000,250):
        generateOct(window,xloc,300)
        poly = ((xloc-90,395),(xloc-95,390),(xloc-95,330),(xloc+95,330),(xloc+95,390),(xloc+90,395))
        pygame.draw.polygon(window,DirtBrown,poly)
        pygame.draw.rect(window,GrassGreen,(xloc-95,330,190,11))

    pygame.draw.line(window,Black,(470,285),(530,285),5)
    pygame.draw.line(window,Black,(470,285),(470,315),5)
    pygame.draw.line(window,Black,(530,285),(530,315),5)
    pygame.draw.line(window,Black,(470,315),(530,315),5)
    pygame.draw.circle(window,Black,(470,315),15,5)
    pygame.draw.circle(window,Black,(530,315),15,5)

    pygame.draw.line(window,Black,(220,295),(280,295),5)
    pygame.draw.line(window,Black,(220,295),(220,315),5)
    pygame.draw.line(window,Black,(280,295),(280,315),5)
    pygame.draw.line(window,Black,(220,315),(280,315),5)
    pygame.draw.circle(window,Black,(220,315),15,5)
    pygame.draw.circle(window,Black,(280,315),15,5)

    pygame.draw.line(window,Black,(710,275),(790,275),5)
    pygame.draw.line(window,Black,(710,275),(710,315),5)
    pygame.draw.line(window,Black,(790,275),(790,315),5)
    pygame.draw.line(window,Black,(710,315),(790,315),5)
    pygame.draw.circle(window,Black,(710,315),15,5)
    pygame.draw.circle(window,Black,(790,315),15,5)

def dirtSize(dif,land):
    if dif == "easy":
        Dirt1width = 340
        Dirt2width = 340
        Dirt2X = 660
    elif dif == "normal":
        Dirt1width = 240
        Dirt2width = 240
        Dirt2X = 760
    elif dif == "hard":
        Dirt1width = 140
        Dirt2width = 140
        Dirt2X = 860

    if land == 1:
        Dirt1height = 200
        Dirt2height = 200
        Dirt1Y = 400
        Dirt2Y = 400
    elif land == 2:
        Dirt1height = math.ceil((200 + ((Dirt2X-Dirt1width)*(17/100))/2)/20)*20
        Dirt2height = math.ceil((200 - ((Dirt2X-Dirt1width)*(17/100))/2)/20)*20
        Dirt1Y = 600 - Dirt1height
        Dirt2Y = 600 - Dirt2height
    elif land == 3:
        Dirt1height = math.ceil((200 - ((Dirt2X-Dirt1width)*(17/100))/2)/20)*20
        Dirt2height = math.ceil((200 + ((Dirt2X-Dirt1width)*(17/100))/2)/20)*20
        Dirt1Y = 600 - Dirt1height
        Dirt2Y = 600 - Dirt2height

    return Dirt1Y,Dirt1width,Dirt1height,Dirt2X,Dirt2Y,Dirt2width,Dirt2height


def BackDrop(dif,land,window,build = False):

    window.fill((135,206,235))

    if dif != "" and land != "":
        Dirt1Y,Dirt1width,Dirt1height,Dirt2X,Dirt2Y,Dirt2width,Dirt2height = dirtSize(dif,land)

        dirt1 = {'shape':pygame.Rect(0,Dirt1Y,Dirt1width,Dirt1height),'colour':DirtBrown}
        dirt2 = {'shape':pygame.Rect(Dirt2X,Dirt2Y,Dirt2width,Dirt2height),'colour':DirtBrown}
        grass1 = {'shape':pygame.Rect(0,Dirt1Y,Dirt1width,10),'colour':GrassGreen}
        grass2 = {'shape':pygame.Rect(Dirt2X,Dirt2Y,Dirt2width,10),'colour':GrassGreen}        


    else:
        dirt1 = {'shape':pygame.Rect(0,410,150,190),'colour':DirtBrown}
        dirt2 = {'shape':pygame.Rect(850,410,150,190),'colour':DirtBrown}
        grass1 = {'shape':pygame.Rect(0,400,150,10),'colour':GrassGreen}
        grass2 = {'shape':pygame.Rect(850,400,150,10),'colour':GrassGreen}
        font = pygame.font.SysFont(None,90)
        text1 = font.render('Bridge Builder', True,White,None)
        text1Rect = text1.get_rect()
        text1Rect.centerx = window.get_rect().centerx
        text1Rect.centery = 75
        text2 = font.render('Bridge Builder', True,Black,None)
        text2Rect = text2.get_rect()
        text2Rect.centerx = window.get_rect().centerx - 5
        text2Rect.centery = 70
        window.blit(text2,text2Rect)
        window.blit(text1,text1Rect)

    cloudCircle11 = {'colour':CloudWhite,'pos':(100,150),'radius':50}
    cloudCircle12 = {'colour':CloudWhite,'pos':(200,150),'radius':50}
    cloudCircle13 = {'colour':CloudWhite,'pos':(150,125),'radius':45}
    cloudCircle21 = {'colour':CloudWhite,'pos':(800,250),'radius':50}
    cloudCircle22 = {'colour':CloudWhite,'pos':(900,250),'radius':50}
    cloudCircle23 = {'colour':CloudWhite,'pos':(850,225),'radius':45}
    cloudRect1 = {'shape':pygame.Rect(100,150,100,50),'colour':CloudWhite}
    cloudRect2 = {'shape':pygame.Rect(800,250,100,50),'colour':CloudWhite}


    circles = [cloudCircle11,cloudCircle12,cloudCircle13,cloudCircle21,cloudCircle22,cloudCircle23]
    ocean = True
    for xloc in range(0,1000,50):
        if ocean == True:
            colour = oceanBlue
            ocean = False
        else:
            colour = skyBlue
            ocean = True
        circles.append({'colour':colour,'pos':(xloc,550),'radius':25})

    pygame.draw.rect(window,oceanBlue,pygame.Rect(0,550,1000,50))
    boxes = [cloudRect1,cloudRect2,dirt1,dirt2,grass1,grass2]
    for circle in circles:
        pygame.draw.circle(window,circle['colour'],circle['pos'],circle['radius'],0)
    for box in boxes:
        pygame.draw.rect(window,box['colour'],box['shape'])

    if dif != "" and land != "" and build == True:
        for xloc in range(0,1020,20):
            pygame.draw.line(window,Black,(xloc,0),(xloc,600),1)
        for yloc in range(0,620,20):
            pygame.draw.line(window,Black,(0,yloc),(1000,yloc),1)


def dotLoc(dif,land):
    mouseLocX,mouseLocY = pygame.mouse.get_pos()
    dotLocMeterX = round(mouseLocX/20)
    dotLocMeterY = round(mouseLocY/20)
    
    Dirt1Y,Dirt1width,Dirt1height,Dirt2X,Dirt2Y,Dirt2width,Dirt2height = dirtSize(dif,land)
    
    xBound1 = math.floor(Dirt1width/20)
    xBound2 = math.ceil(Dirt2X/20)
    yBound1 = math.ceil(Dirt1Y/20)
    yBound2 = math.ceil(Dirt2Y/20)

    if dotLocMeterX < xBound1 and dotLocMeterY > yBound1:
        if (xBound1-dotLocMeterX) < (dotLocMeterY-yBound1):
            dotLocMeterX = xBound1
        elif (xBound1-dotLocMeterX) > (dotLocMeterY-yBound1):
            dotLocMeterY = yBound1
        else:
            dotLocMeterY = yBound1
    elif dotLocMeterX > xBound2 and dotLocMeterY > yBound2:
        if (dotLocMeterX-xBound2) < (dotLocMeterY-yBound2):
            dotLocMeterX = xBound2
        elif (dotLocMeterX-xBound2) > (dotLocMeterY-yBound2):
            dotLocMeterY = yBound2
        else:
            dotLocMeterY = yBound2

    dotLocPixelX = dotLocMeterX*20
    dotLocPixelY = dotLocMeterY*20

    return dotLocPixelX,dotLocPixelY

def drawDot(window,dif,land,colour):
    x,y = dotLoc(dif,land)
    pygame.draw.circle(window,Black,(x,y),6,0)
    pygame.draw.circle(window,colour,(x,y),4,0)

    return x,y

def drawJoint(window,point):
    x,y = point
    pygame.draw.rect(window,Black,(x-6,y-6,12,12))
    pygame.draw.rect(window,LightBrown,(x-4,y-4,8,8))

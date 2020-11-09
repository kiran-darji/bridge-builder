import pygame,sys,Graphics,Classes,BridgeData,Save
from pygame.locals import *

def loadBridge(bridgeID):
    jointList = []
    bridgeFile,dif,land = BridgeData.getBridgeFile(bridgeID)
    bridgeFile = eval(bridgeFile.strip("'"))
    jointNum = len(bridgeFile)
    materialStack = []
    added = False
    for joint in bridgeFile:
        jointX,jointY = bridgeFile[joint]['location']
        jointList.append({'index':int(joint),'point':(jointX*20,600 - jointY*20)}) 
    for joint in bridgeFile:
        joint1 = int(joint)
        for connectedJoint in bridgeFile[joint]['connectedJoints']:
            joint2 = int(connectedJoint['joint'])
            for material in materialStack:
                if (material.getJoint1() == joint1 and material.getJoint2() == joint2) or (material.getJoint1() == joint2 and material.getJoint2() == joint1):
                    added = True
            if added == False:
                if connectedJoint['material'] == 'Steel':
                    item = Classes.Steel()
                elif connectedJoint['material'] == 'Wood':
                    item = Classes.Wood()
                elif connectedJoint['material'] == 'Road':
                    item = Classes.Road()
                elif connectedJoint['material'] == 'Rope':
                    item = Classes.Rope()
                elif connectedJoint['material'] == 'Cable':
                    item = Classes.Cable()
                item.setjoint1(joint1)
                item.setjoint2(joint2)
                materialStack.append(item)
            else:
                added = False

    for material in materialStack:
        for joint in jointList:
            if int(material.getJoint1()) == int(joint['index']):
                jointX,jointY = joint['point']
                material.setCo1(jointX,jointY)
            elif int(material.getJoint2()) == int(joint['index']):
                jointX,jointY = joint['point']
                material.setCo2(jointX,jointY)
                    

    return [materialStack,jointList,jointNum,dif,land]

def deleteExcessJoint(jointList,materialStack):
    toDelete = []
    for joint in jointList:
        numOfConnectedMaterials = 0
        for material in materialStack:
            if joint['index'] == material.getJoint1() or joint['index'] == material.getJoint2():
                numOfConnectedMaterials += 1
        if numOfConnectedMaterials == 0:
            toDelete.append(joint)
    for joint in toDelete:
        jointList.remove(joint)

def jointClick(jointList,dotX,dotY):
    for joint in jointList:
        jointX,jointY = joint['point']
        rect = pygame.Rect(jointX-6,jointY-6,12,12)
        if rect.collidepoint((dotX,dotY)) == True:
            return joint['index']
    return 0

def allowConnect(materialStack,item,dotX,dotY):
    for material in materialStack:
        if ((material.getStart() == item.getStart()) and (material.getEnd() == (dotX,dotY))) or ((material.getStart() == (dotX,dotY)) and (material.getEnd() == item.getStart())):
            item.errorTrue()

def stckbtnclk(stickButtons):
    for button in stickButtons:
        if stickButtons[button].ifClick():
            return button
    return ""

def turnOn(btn,stickButtons):
    for button in stickButtons:
        if button == btn:
            stickButtons[btn].turnOn()
        else:
            stickButtons[button].turnOff()
    

def buttonOn(stickButtons):
    for button in stickButtons:
        if stickButtons[button].getOn():
            return button
    return ""

def Main(info,window):
    
    stickButtons = {
    'steel':Classes.stickButton('   Steel   ',100,550),
    'wood':Classes.stickButton('   Wood  ',300,550),
    'road':Classes.stickButton('Concrete',500,550),
    'rope':Classes.stickButton('   Rope   ',700,550),
    'cable':Classes.stickButton('   Cable  ',900,550),
    'delete':Classes.stickButton('   Delete   ',900,50,(223,12,12)),
    'quit':Classes.stickButton('   Quit   ',100,50,(223,12,12)),
    'save':Classes.stickButton('  Save    ',300,50,(34,204,0)),
    'undo':Classes.stickButton('   Undo   ',700,50,(223,12,12)),
    'test':Classes.stickButton('   Test   ',500,50)
    }
    
    if info['loadBridge'] == False:
        materialStack = []
        jointList = []
        jointNum = 0
    else:
        materialStack,jointList,jointNum,dif,land = loadBridge(info['bridgeID'])
        info['dif'] = dif.strip("'")
        info['land'] = land

    clickStage = "PlaceMaterial1"
    click = False
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                release = True

        Graphics.BackDrop(info['dif'],info['land'],window,True)

        Material = buttonOn(stickButtons)
        if Material == "delete":
            clickStage = "Delete"
        elif Material == "quit":
            clickStage = "Quit"
            click = True
        elif Material == "save":
            clickStage = "Save"
            click = True
        elif Material == "undo":
            clickStage = "Undo"
            click = True
        elif Material == "test":
            clickStage = "Test"
            click = True

        for material in materialStack:
            material.Draw(window)
        for material in jointList:
            Graphics.drawJoint(window,material['point'])

        if clickStage == "PlaceMaterial1":
            for button in stickButtons:
                stickButtons[button].create(window)
        elif clickStage == "PlaceMaterial2":
            item.updateLocation(dotX,dotY)
            item.checkPlacement()
            allowConnect(materialStack,item,dotX,dotY)
            item.Draw(window)

        if Material != "":
            if Material == "delete":
                dotX,dotY = Graphics.drawDot(window,info['dif'],info['land'],(233,12,12))
            else:
                dotX,dotY = Graphics.drawDot(window,info['dif'],info['land'],(255,255,255))



        if click:
            if clickStage == "PlaceMaterial1":
                if Material != "" and stckbtnclk(stickButtons) == "":
                    if Material == "steel":
                        item = Classes.Steel()
                    elif Material == "wood":
                        item = Classes.Wood()
                    elif Material == "road":
                        item = Classes.Road()
                    elif Material == "rope":
                        item = Classes.Rope()
                    elif Material == "cable":
                        item = Classes.Cable()
                    item.setCo1(dotX,dotY)
                    clickStage = "PlaceMaterial2"
                    jointPoints = []
                    for joint in jointList:
                        jointPoints.append(joint['point'])
                    if (dotX,dotY) not in jointPoints:
                        jointNum += 1
                        jointList.append({'index':jointNum,'point':(dotX,dotY)})
                    for joint in jointList:
                        if joint['point'] == (dotX,dotY):
                            item.setjoint1(joint['index'])
                else:
                    turnOn(stckbtnclk(stickButtons),stickButtons)
            elif clickStage == "PlaceMaterial2":
                if item.getError() == False:
                    jointPoints = []
                    for joint in jointList:
                        jointPoints.append(joint['point'])
                    if (dotX,dotY) not in jointPoints:
                        jointNum += 1
                        jointList.append({'index':jointNum,'point':(dotX,dotY)})
                    for joint in jointList:
                        if joint['point'] == (dotX,dotY):
                            item.setjoint2(joint['index'])
                    materialStack.append(item)
                    clickStage = "PlaceMaterial1"
            elif clickStage == "Delete":
                jointClicked = jointClick(jointList,dotX,dotY)
                jointCount = 0
                cap = False
                toDelete = []
                if jointClicked != 0:
                    for joint in jointList:
                        if joint['index'] == jointClicked:
                            cap = True
                        if cap == False:
                            jointCount+=1
                    del jointList[jointCount]
                    for material in materialStack:
                        if material.getJoint1() == jointClicked or material.getJoint2() == jointClicked:
                            toDelete.append(material)
                    for material in toDelete:                            
                        materialStack.remove(material)
                    deleteExcessJoint(jointList,materialStack)
                clickStage = "PlaceMaterial1"
                stickButtons['delete'].turnOff()
            elif clickStage == "Quit":
                info['build'] = False
                return ["sec",info]
            elif clickStage == "Save":
                if len(materialStack) != 0:
                    Save.Main(window,jointList,materialStack,info)
                clickStage = "PlaceMaterial1"
                stickButtons['save'].turnOff()
            elif clickStage == "Undo":
                if len(materialStack) != 0:
                    del materialStack[-1]
                clickStage = "PlaceMaterial1"
                stickButtons['undo'].turnOff()
                deleteExcessJoint(jointList,materialStack)
            elif clickStage == "Test":
                if len(materialStack) != 0:
                    Save.Main(window,jointList,materialStack,info)
                    info['build'] = False
                    return ["chooseVehicle",info]
                clickStage = "PlaceMaterial1"
                stickButtons['test'].turnOff()
            click = False
        clock.tick()
        fps = clock.get_fps()
        #print(fps)
        pygame.display.update()

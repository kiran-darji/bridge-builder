import Classes
import pygame,sys
import BridgeData
import os

def checkSaveName(inputboxes,info,adjacencyList):
    checkList = [" ", ";", "=", "'", '"']
    error = []
    emptyCount = 0
    bridgeID = ""
    for box in inputboxes:
        for char in checkList:
            if (inputboxes[box].getCap() == "") or (char in inputboxes[box].getCap()):
                emptyCount += 1
    if emptyCount > 0:
        text = "All fields must be entered and cannot contain ;, =, ' or \""
        error.append(text)
    
    if error == []:
        name = inputboxes['name'].getCap()
        nameState = BridgeData.findBridge(name,info['User_ID'])
        if nameState == "Taken":
            error.append("You have used this name already")
        elif nameState == "Error":
            error.append("Error connecting to database")

    if error == []:
        fileName = (name+"_"+str(info['User_ID']))
        with open(fileName,'w') as File:
            File.write(str(adjacencyList))
        with open(fileName,'r') as File:
            openedFile = File.read()
            connect = BridgeData.addBridge(name,openedFile,info)
        os.remove(fileName)
        if connect != "":
            error.append("Error connecting to database")
        else:
            bridgeID = BridgeData.getBridgeID(name,info['User_ID'])

    return [error,bridgeID]
    
def PopUpMessage(text,window):
    center = (window.get_rect().centerx, window.get_rect().centery)
    y = 50*(len(text)+1)
    message = Classes.TextBox(text,y,950,center,(233,12,12))
    message.create(window)

def createSave(buttons,inputboxes,window,error):
    buttons['save'].create(window)
    buttons['cancel'].create(window)
    if error == True:
        buttons['ok'].create(window)
    height = 100
    width = 800
    x = window.get_rect().centerx
    y = 280
    center = (x,y)
    text = Classes.TextBox("",height,width,center)
    text.create(window)
    inputboxes['name'].create(window)

def findConnections(index,materials):
    connectedTo = []
    for material in materials:
        if index == material.getJoint1():
            connectedTo.append({'joint':material.getJoint2(),'material':material.getMaterial()})
        elif index == material.getJoint2():
            connectedTo.append({'joint':material.getJoint1(),'material':material.getMaterial()})
    return connectedTo

def Main(window,jointList,materialStack,info):
    adjacencyList = {}
    for joint in jointList:
        index = joint['index']
        x,y = joint['point']
        x /= 20
        y = 30 - y/20
        location = (int(x),int(y))
        connectedJoints = findConnections(index,materialStack)
        adjacencyList[str(index)] = {'location':location, 'connectedJoints':connectedJoints}
    buttons = {
    'save':Classes.Button('    Save    ',650,500),
    'cancel':Classes.Button('   Cancel   ',350,500),
    'ok':Classes.Button('     OK     ',500,500,(233,12,12))
}
    inputboxes = {
    'name':Classes.InputBox("Bridge Name:",365,250,470,60)
}
    click = False
    Type = False
    error = False

    if info['loadBridge'] == False:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                elif event.type == pygame.KEYDOWN:
                    Type = True
                    if event.key == pygame.K_BACKSPACE:
                        char = 'back'
                    else:
                        char = event.unicode

            createSave(buttons,inputboxes,window,error)
            if error == True:
                PopUpMessage(sentences,window)

            if click == True:
                if error == False:
                    inputboxes['name'].deActive()
                    if buttons['save'].ifClick():
                        sentences,bridgeID = checkSaveName(inputboxes,info,adjacencyList)
                        info['bridgeID'] = bridgeID
                        if sentences != []:
                            error = True
                        else:
                            error = False
                            info['loadBridge'] = True
                            return
                    elif buttons['cancel'].ifClick():
                        return
                    elif inputboxes['name'].ifClick():
                        inputboxes['name'].makeActive()
                else:
                    if buttons['ok'].ifClick():
                        error = False
                        return

                click = False
            

            if Type == True:
                if inputboxes['name'].getActive():
                    if char == 'back':
                        inputboxes['name'].Back()
                    elif (char != 'back') and (inputboxes['name'].getCapLength() < 20):
                        inputboxes['name'].Add(char)
                Type = False

            pygame.display.update()
    
    else:
        fileName = ("Temp")
        with open(fileName,'w') as File:
            File.write(str(adjacencyList))
        with open(fileName,'r') as File:
            openedFile = File.read()
            BridgeData.updateBridge(info['bridgeID'],adjacencyList)
        os.remove(fileName)

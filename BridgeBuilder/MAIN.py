import pygame,sys,Graphics,Classes,BridgeData,Build,Test,hashlib
from pygame.locals import *

White = (255,255,255)
Red = (233,12,12)
LeafGreen = (97,138,61)
RoyalPurple = (120,81,169)
WarmBlue = (30,144,255)
BirchWhite = (248,223,161)
Pink = (255,105,180)

def PopUpMessage(text,window):
    center = (window.get_rect().centerx, window.get_rect().centery)
    height = 50*(len(text)+1)
    message = Classes.TextBox(text,height,950,center,Red)
    message.create(window)

def createButtonsbridgeOp(window,bridgeName,bridgeDate,buttons,error):
    buttons['edit'].create(window)
    buttons['test'].create(window)
    buttons['delete'].create(window)
    buttons['back5'].create(window)
    cap = ("%s Last Edited: %s"%(bridgeName,bridgeDate))
    height = 50
    width = 600
    x = window.get_rect().centerx
    y = 150
    center = (x,y)
    text = Classes.TextBox(cap,height,width,center)
    text.create(window)
    if error:
        buttons['yes'].create(window)
        buttons['cancel'].create(window)
        PopUpMessage(["Are you sure you want to delete this bridge?"],window)        

def createButtonsLoad(buttons,window,loadMenu,User_ID):
    font = pygame.font.SysFont(None,50)
    listOfBridgeID = []
    listOfBridgeNames = []
    listOfBridgeDates = []
    buttonsOnScreen = 0
    numOfScreens = 0
    upButton = False
    downButton = False
    results = BridgeData.getBridges(User_ID)
    start = loadMenu*5
    end = start + len(results)%5

    if len(results) != 0:
        if len(results)%5 != 0:
            numOfScreens = len(results)//5 + 1
            if loadMenu == numOfScreens - 1:
                for bridge in range(start,end):
                    listOfBridgeID.append(results[bridge][0])
                    listOfBridgeNames.append(results[bridge][1].replace("'",""))
                    date = ("%s/%s/%s"%(results[bridge][2],results[bridge][3],results[bridge][4]))
                    listOfBridgeDates.append(date)
                    buttonsOnScreen += 1
            else:
                for bridge in range(start,start+5):
                    listOfBridgeID.append(results[bridge][0])
                    listOfBridgeNames.append(results[bridge][1].replace("'",""))
                    date = ("%s/%s/%s"%(results[bridge][2],results[bridge][3],results[bridge][4]))
                    listOfBridgeDates.append(date)
                    buttonsOnScreen += 1
        else:
            numOfScreens = len(results)//5
            for bridge in range(start,start+5):
                listOfBridgeID.append(results[bridge][0])
                listOfBridgeNames.append(results[bridge][1].replace("'",""))
                date = ("%s/%s/%s"%(results[bridge][2],results[bridge][3],results[bridge][4]))
                listOfBridgeDates.append(date)
                buttonsOnScreen += 1
    else:
        height = 100
        width = 600
        x = window.get_rect().centerx
        y = window.get_rect().centery
        center = (x,y)
        text = Classes.TextBox("You have no bridges",height,width,center)
        text.create(window)
        
    
    if buttonsOnScreen >= 1:
        buttons['bridge1'].create(window)
    if buttonsOnScreen >= 2:
        buttons['bridge2'].create(window)
    if buttonsOnScreen >= 3:
        buttons['bridge3'].create(window)
    if buttonsOnScreen >= 4:
        buttons['bridge4'].create(window)
    if buttonsOnScreen == 5:
        buttons['bridge5'].create(window)
    if loadMenu != 0:
        buttons['up'].create(window)
        upButton = True
        pygame.draw.line(window,White,(500,120),(480,140),10)
        pygame.draw.line(window,White,(500,120),(520,140),10)
    if loadMenu < numOfScreens-1:
        buttons['down'].create(window)
        downButton = True
        pygame.draw.line(window,White,(500,500),(480,480),10)
        pygame.draw.line(window,White,(500,500),(520,480),10)
    buttons['back5'].create(window)

    for bridgeName in range(0,len(listOfBridgeNames)):
        text = font.render(listOfBridgeNames[bridgeName],True,(255,255,255),None)
        textRect = text.get_rect()
        textRect.centerx = window.get_rect().centerx
        textRect.centery = 190 + bridgeName*60

        window.blit(text,textRect)
 
    return [listOfBridgeID,listOfBridgeNames,listOfBridgeDates,buttonsOnScreen,upButton,downButton]


def createButtonsInitial(buttons,window):
    buttons['loginOp'].create(window)
    buttons['registerOp'].create(window)
    buttons['quit'].create(window)

def createLogin(buttons,inputboxes,window,error):
    buttons['login'].create(window)
    buttons['back'].create(window)
    if error == True:
        buttons['ok'].create(window)
    height = 250
    width = 700
    x = window.get_rect().centerx
    y = window.get_rect().centery
    center = (x,y)
    text = Classes.TextBox("",height,width,center)
    text.create(window)
    inputboxes['Lusername'].create(window)
    inputboxes['Lpassword'].create(window)

def createRegister(buttons,inputboxes,window,error):
    buttons['register'].create(window,error)
    buttons['back2'].create(window,error)
    if error == True:
        buttons['ok'].create(window)
    height = 400
    width = 950
    x = window.get_rect().centerx
    y = window.get_rect().centery + 15
    center = (x,y)
    text = Classes.TextBox("",height,width,center)
    text.create(window)
    inputboxes['Rusername'].create(window)
    inputboxes['Rpassword'].create(window)
    inputboxes['RpasswordC'].create(window)
    inputboxes['first'].create(window)
    inputboxes['sec'].create(window)
    inputboxes['email'].create(window)


def createButtonsMain(buttons,window):
    buttons['play'].create(window)
    buttons['instruc'].create(window)
    buttons['logout'].create(window)

def createButtonsPlay(buttons,window):
    buttons['new'].create(window)
    buttons['load'].create(window)
    buttons['back3'].create(window)

def createButtonsLand(buttons,window):
    buttons['flat'].create(window)
    buttons['highlow'].create(window)
    buttons['lowhigh'].create(window)
    buttons['back5'].create(window)

def createButtonsDif(buttons,window):
    buttons['easy'].create(window)
    buttons['normal'].create(window)
    buttons['hard'].create(window)
    buttons['back5'].create(window)

def createButtonsVehicle(buttons,window):
    buttons['bike'].create(window)
    buttons['car'].create(window)
    buttons['truck'].create(window)
    buttons['back5'].create(window)

def createInstruc(buttons,window):
    buttons['back4'].create(window)
    cap = 'sample text'
    height = 350
    width = 900
    x = window.get_rect().centerx
    y = window.get_rect().centery
    center = (x,y)
    text = Classes.TextBox(cap,height,width,center)
    text.create(window)

def DeActivateInputs(inputboxes,current):
    for box in inputboxes:
        if box != current:
            inputboxes[box].deActive()

def checkLogin(inputboxes):
    checkList = [" ", ";", "=", "'", '"']
    error = []
    User_ID = ""
    emptyCount = 0
    invalidCharCount = 0
    for box in inputboxes:
        if (box == "Lusername") or (box == "Lpassword"):
            for char in checkList:
                if inputboxes[box].getCap() == "":
                    emptyCount += 1
                elif char in inputboxes[box].getCap():
                    invalidCharCount += 1
    if emptyCount > 0:
        text = "All fields must be entered"
        error.append(text)
    if invalidCharCount > 0:
        text = "Incorrect details"
        error.append(text)

    if error == []:
        Hash = hashlib.sha512()
        username = inputboxes['Lusername'].getCap()
        passCap = bytes(inputboxes['Lpassword'].getCap(), encoding='utf-8')
        Hash.update(passCap)
        password = Hash.hexdigest()

        connect = BridgeData.findUser(username,password)

        if connect == "Not":
            error.append("Incorrect details")
        elif connect == "Error":
            error.append("Error connecting to database")
        else:
            User_ID = BridgeData.getUser_ID(username)

        if User_ID == "":
            error.append("Error connecting to the database")

    return error,User_ID


def checkRegister(inputboxes):
    checkList = [" ", ";", "=", "'", '"']
    error = []
    emptyCount = 0
    for box in inputboxes:
        if (box != "Lusername") and (box != "Lpassword"):
            for char in checkList:
                if (inputboxes[box].getCap() == "") or (char in inputboxes[box].getCap()):
                    emptyCount += 1
    if emptyCount > 0:
        text = "All fields must be entered and cannot contain ;, =, ' or \""
        error.append(text)
    if (not("@" in inputboxes['email'].getCap())) and (inputboxes['email'].getCap() != ""):
        text = "Please enter a valid email"
        error.append(text)
    if inputboxes['Rpassword'].getCap() != inputboxes['RpasswordC'].getCap():
        text = "Passwords do not match"
        error.append(text)

    if error == []:
        username = inputboxes['Rusername'].getCap()
        UsernameState = BridgeData.findUsername(username)
        if UsernameState != "":
            if UsernameState == "Taken":
                error.append("Username taken")
            elif UsernameState == "Error":
                error.append("Error connecting to database")

        email = inputboxes['email'].getCap()
        EmailState = BridgeData.findEmail(email)
        if EmailState != "":
            if EmailState == "Taken":
                error.append("Email taken")
            elif EmailState == "Error":
                error.append("Error connecting to database")
    
    if error == []:
        Hash = hashlib.sha512()
        first = inputboxes['first'].getCap()
        sec = inputboxes['sec'].getCap()
        email = inputboxes['email'].getCap()
        username = inputboxes['Rusername'].getCap()
        passCap = bytes(inputboxes['Rpassword'].getCap(), encoding='utf-8')
        Hash.update(passCap)
        password = Hash.hexdigest()
        
        connect = BridgeData.addUser(first,sec,email,username,password)

        if connect != "":
            error.append("Error connecting to database")

    return error


def menuLoop(Menu,window,info):
    User_ID = info['User_ID']
    bridgeID = info['bridgeID']
    
    buttons = {
    'loginOp':Classes.Button('       Login       ',window.get_rect().centerx,250),
    'registerOp':Classes.Button('    Register    ',window.get_rect().centerx,350),
    'quit':Classes.Button('        Quit         ',window.get_rect().centerx,450),
    'login':Classes.Button('        Login        ',650,500),
    'back':Classes.Button('        Back        ',350,500),
    'register':Classes.Button('    Register    ',650,555),
    'back2': Classes.Button('        Back        ',350,555),
    'play':Classes.Button('        Play        ',window.get_rect().centerx,250),
    'instruc':Classes.Button(' Instructions ',window.get_rect().centerx,350),
    'logout':Classes.Button('       Logout       ',window.get_rect().centerx,450),
    'new':Classes.Button(' New Bridge ',window.get_rect().centerx,250),
    'load':Classes.Button(' Load Bridge ',window.get_rect().centerx,350),
    'back3':Classes.Button('        Back        ',window.get_rect().centerx,450),
    'back4':Classes.Button('        Back        ',window.get_rect().centerx,550),
    'flat':Classes.Button('         Flat        ',500,450),
    'highlow':Classes.Button(' High to Low ',250,450),
    'lowhigh':Classes.Button(' Low to High ',750,450),
    'back5':Classes.Button('       Back       ',500,550),
    'normal':Classes.Button('      Normal     ',500,450),
    'easy':Classes.Button('         Easy        ',250,450),
    'hard':Classes.Button('         Hard        ',750,450),
    'ok':Classes.Button('          OK          ',500,550,Red),
    'bridge1':Classes.Button('                    ',500,190,LeafGreen),
    'bridge2':Classes.Button('                    ',500,250,RoyalPurple),
    'bridge3':Classes.Button('                    ',500,310,WarmBlue),
    'bridge4':Classes.Button('                    ',500,370,BirchWhite),
    'bridge5':Classes.Button('                    ',500,430,Pink),
    'up':Classes.Button('        ',500,130,width=30,height=15),
    'down':Classes.Button('        ',500,490,width=30,height=15),
    'edit':Classes.Button('       Edit      ',500,250),
    'test':Classes.Button('       Test      ',500,350),
    'delete':Classes.Button('     Delete    ',500,450,Red),
    'yes':Classes.Button('        Yes        ',700,500,Red),
    'cancel':Classes.Button('     Cancel     ',300,500,Red),
    'bike':Classes.Button('      Bike     ',250,450),
    'car':Classes.Button('         Car        ',500,450),
    'truck':Classes.Button('         Truck        ',750,450),
    }

    inputboxes = {
    'Lusername':Classes.InputBox("Username:",365,200,470,60),
    'Lpassword':Classes.InputBox("Password:",365,300,470,60),
    'first':Classes.InputBox("First Name:",365,123,470,60),
    'sec':Classes.InputBox("Surname:",365,188,470,60),
    'email':Classes.InputBox("Email:",150,253,810,60),
    'Rusername':Classes.InputBox("Username:",365,318,470,60),
    'Rpassword':Classes.InputBox("Password:",365,383,470,60),
    'RpasswordC':Classes.InputBox("Re-Type:",365,448,470,60)
    }

    menu = Menu
    loadMenu = 0
    #clock = pygame.time.Clock()
    click = False
    Type = False
    error = False
    loadBridge = False
    vehicle = ""
    dif = ""
    landscape= ""
    
    while menu != "build" and menu != "test":
        for event in pygame.event.get():
            if event.type == QUIT:
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

        Graphics.BackDrop("","",window)

        if menu == "initial":
            createButtonsInitial(buttons,window)
        elif menu == "login":
            createLogin(buttons,inputboxes,window,error)
            if error == True:
                PopUpMessage(sentences,window)
        elif menu == "register":
            createRegister(buttons,inputboxes,window,error)
            if error == True:
                PopUpMessage(sentences,window)
        elif menu == "main":
            createButtonsMain(buttons,window)
        elif menu == "sec":
            createButtonsPlay(buttons,window)
        elif menu == "instruc":
            createInstruc(buttons,window)
        elif menu == "LandOp":
            Graphics.LandImage(window)
            createButtonsLand(buttons,window)
        elif menu == "Dif":
            Graphics.DifImage(window,landscape)
            createButtonsDif(buttons,window)
        elif menu == "load":
            listOfBridgeID,listOfBridgeNames,listOfBridgeDates,buttonsOnScreen,upButton,downButton = createButtonsLoad(buttons,window,loadMenu,User_ID)
        elif menu == "bridgeOp":
            createButtonsbridgeOp(window,bridgeName,bridgeDate,buttons,error)
        elif menu == "chooseVehicle":
            Graphics.vehicleImage(window)
            createButtonsVehicle(buttons,window)

        if click == True:
            if menu == 'initial':
                if buttons['loginOp'].ifClick():
                    menu = 'login'
                elif buttons['registerOp'].ifClick():
                    menu = 'register'
                elif buttons['quit'].ifClick():
                    pygame.quit()
                    sys.exit()
            elif menu == 'login':
                if error == False:
                    if inputboxes['Lusername'].ifClick():
                        inputboxes['Lusername'].makeActive()
                        DeActivateInputs(inputboxes,"Lusername")
                    elif inputboxes['Lpassword'].ifClick():
                        inputboxes['Lpassword'].makeActive()
                        DeActivateInputs(inputboxes,"Lpassword")
                    elif buttons['login'].ifClick():
                        sentences,User_ID = checkLogin(inputboxes)
                        if sentences != []:
                            error = True
                        else:
                            error = False
                            menu = "main"
                        DeActivateInputs(inputboxes," ")
                    elif buttons['login'].ifClick():
                        menu = 'initial'
                        DeActivateInputs(inputboxes," ")
                    else:
                        DeActivateInputs(inputboxes," ")
                else:
                    if buttons['ok'].ifClick():
                        error = False
            elif menu == 'register':
                if error == False:
                    if inputboxes['first'].ifClick():
                        inputboxes['first'].makeActive()
                        DeActivateInputs(inputboxes,"first")
                    elif inputboxes['sec'].ifClick():
                        inputboxes['sec'].makeActive()
                        DeActivateInputs(inputboxes,"sec")
                    elif inputboxes['email'].ifClick():
                        inputboxes['email'].makeActive()
                        DeActivateInputs(inputboxes,"email")
                    elif inputboxes['Rusername'].ifClick():
                        inputboxes['Rusername'].makeActive()
                        DeActivateInputs(inputboxes,"Rusername")
                    elif inputboxes['Rpassword'].ifClick():
                        inputboxes['Rpassword'].makeActive()
                        DeActivateInputs(inputboxes,"Rpassword")
                    elif inputboxes['RpasswordC'].ifClick():
                        inputboxes['RpasswordC'].makeActive()
                        DeActivateInputs(inputboxes,"RpasswordC")
                    elif buttons['register'].ifClick():
                        sentences = checkRegister(inputboxes)
                        if sentences != []:
                            error = True
                        else:
                            error = False
                            menu = 'login'
                        DeActivateInputs(inputboxes," ")
                    elif buttons['back2'].ifClick():
                        menu = 'initial'
                        DeActivateInputs(inputboxes," ")
                    else:
                        DeActivateInputs(inputboxes," ")
                else:
                    if buttons['ok'].ifClick():
                        error = False
            elif menu == 'main':
                if buttons['play'].ifClick():
                    menu = 'sec'
                elif buttons['instruc'].ifClick():
                    menu = 'instruc'
                elif buttons['logout'].ifClick():
                    menu = 'initial'
            elif menu == "sec":
                if buttons['new'].ifClick():
                    menu = "LandOp"
                elif buttons['load'].ifClick():
                    menu = "load"
                elif buttons['back3'].ifClick():
                    menu = "main"
            elif menu == "instruc":
                if buttons['back4'].ifClick():
                    menu = "main"
            elif menu == "LandOp":
                if buttons['flat'].ifClick():
                    landscape = 1
                    menu = "Dif"
                elif buttons['highlow'].ifClick():
                    landscape = 2
                    menu = "Dif"
                elif buttons['lowhigh'].ifClick():
                    menu = "Dif"
                    landscape = 3
                elif buttons['back5'].ifClick():
                    menu = "sec"
            elif menu == "Dif":
                if buttons['normal'].ifClick():
                    dif = "normal"
                    menu = "build"
                    loadBridge = False
                elif buttons['easy'].ifClick():
                    dif = "easy"
                    menu = "build"
                    loadBridge = False
                elif buttons['hard'].ifClick():
                    menu = "build"
                    dif = "hard"
                    loadBridge = False
                elif buttons['back5'].ifClick():
                    menu = "LandOp"
            elif menu == "load":
                bridgeOp = 0
                if buttonsOnScreen >= 1: 
                    if buttons['bridge1'].ifClick():
                        menu = "bridgeOp"
                        bridgeOp = 1
                if buttonsOnScreen >= 2: 
                    if buttons['bridge2'].ifClick():
                        menu = "bridgeOp"
                        bridgeOp = 2
                if buttonsOnScreen >= 3:
                    if buttons['bridge3'].ifClick():
                        menu = "bridgeOp"
                        bridgeOp = 3
                if buttonsOnScreen >= 4: 
                    if buttons['bridge4'].ifClick():
                        menu = "bridgeOp"
                        bridgeOp = 4
                if buttonsOnScreen == 5:
                    if buttons['bridge5'].ifClick():
                        menu = "bridgeOp"
                        bridgeOp = 5
                if bridgeOp != 0:
                    bridgeID = listOfBridgeID[bridgeOp-1]
                    bridgeName = listOfBridgeNames[bridgeOp-1]
                    bridgeDate = listOfBridgeDates[bridgeOp-1]
                if upButton: 
                    if buttons['up'].ifClick():
                        loadMenu -= 1
                if downButton: 
                    if buttons['down'].ifClick():
                        loadMenu += 1
                if buttons['back5'].ifClick():
                    menu = "sec"
            elif menu == "bridgeOp":
                if error == False:
                    if buttons['edit'].ifClick():
                        menu = "build"
                        loadBridge = True
                        dif = ""
                        landscape = ""
                    elif buttons['test'].ifClick():
                        menu = "chooseVehicle"
                    elif buttons['delete'].ifClick():
                        error = True
                    elif buttons['back5'].ifClick():
                        menu = "load"
                else:
                    if buttons['yes'].ifClick():
                        BridgeData.deleteBridge(bridgeID)
                        menu = "load"
                        error = False
                        loadMenu = 0
                    elif buttons['cancel'].ifClick():
                        error = False
            elif menu == "chooseVehicle":
                if buttons['bike'].ifClick():
                    menu = "test"
                    vehicle = "bike"
                elif buttons['car'].ifClick():
                    menu = "test"
                    vehicle = "car"
                elif buttons['truck'].ifClick():
                    menu = "test"
                    vehicle = "truck"
                elif buttons['back5'].ifClick():
                    menu = "load"

            click = False

        if Type == True:
            if menu == 'login':
                if inputboxes['Lusername'].getActive() == True:
                    if char == 'back':
                        inputboxes['Lusername'].Back()
                    elif (char != 'back') and (inputboxes['Lusername'].getCapLength() < 20):
                        inputboxes['Lusername'].Add(char)
                elif inputboxes['Lpassword'].getActive() == True:
                    if char == 'back':
                        inputboxes['Lpassword'].Back()
                    elif (char != 'back') and (inputboxes['Lpassword'].getCapLength() < 20):
                        inputboxes['Lpassword'].Add("X")
            elif menu == 'register':
                if inputboxes['first'].getActive() == True:
                    if char == 'back':
                        inputboxes['first'].Back()
                    elif (char != 'back') and (inputboxes['first'].getCapLength() < 20):
                        inputboxes['first'].Add(char)
                elif inputboxes['sec'].getActive() == True:
                    if char == 'back':
                        inputboxes['sec'].Back()
                    elif (char != 'back') and (inputboxes['sec'].getCapLength() < 20):
                        inputboxes['sec'].Add(char)
                elif inputboxes['email'].getActive() == True:
                    if char == 'back':
                        inputboxes['email'].Back()
                    elif (char != 'back') and (inputboxes['email'].getCapLength() < 50):
                        inputboxes['email'].Add(char)
                elif inputboxes['Rusername'].getActive() == True:
                    if char == 'back':
                        inputboxes['Rusername'].Back()
                    elif (char != 'back') and (inputboxes['Rusername'].getCapLength() < 20):
                        inputboxes['Rusername'].Add(char)
                elif inputboxes['Rpassword'].getActive() == True:
                    if char == 'back':
                        inputboxes['Rpassword'].Back()
                    elif (char != 'back') and (inputboxes['Rpassword'].getCapLength() < 20):
                        inputboxes['Rpassword'].Add("X")
                elif inputboxes['RpasswordC'].getActive() == True:
                    if char == 'back':
                        inputboxes['RpasswordC'].Back()
                    elif (char != 'back') and (inputboxes['RpasswordC'].getCapLength() < 20):
                        inputboxes['RpasswordC'].Add("X")
            Type = False
            char = ""


        #clock.tick()
        #fps = clock.get_fps()
        #print(fps)
        pygame.display.update()

    
    info = {'User_ID':User_ID, 'dif':dif,'land':landscape,'bridgeID':bridgeID, 'loadBridge':loadBridge,'build':False,'test':False,'vehicle':vehicle}

    if menu == "build":
        info['build'] = True
    elif menu == "test":
        info['test'] = True
    
    return info


def Main():
    pygame.init()
    window = pygame.display.set_mode((1000,600),0,32)
    Next = "initial"
    info = {'User_ID':0,'bridgeID':0,'build':False,'test':False}
    while True:
        if info['build'] == False and info['test'] == False:
            info = menuLoop(Next,window,info)
        if info['build']:
            Next,info = Build.Main(info,window)
        if info['test']:
            Next,info = Test.Main(info,window)

Main()

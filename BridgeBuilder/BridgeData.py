import pymysql

def findUsername(username):
    db = pymysql.connect("localhost","Kiran","!winter@2018","BridgeBuilder")
    cursor = db.cursor()
    command = "SELECT * FROM User WHERE Username = '%s';" %(username)
    results = ""
    try:
        cursor.execute(command)
        if len(cursor.fetchall()) > 0:
            results = "Taken"
    except:
        results = "Error"
    db.close()
    return results

def findEmail(email):
    db = pymysql.connect("localhost","Kiran","!winter@2018","BridgeBuilder")
    cursor = db.cursor()
    command = "SELECT * FROM User WHERE Email = '%s';" %(email)
    results = ""
    try:
        cursor.execute(command)
        if len(cursor.fetchall()) > 0:
            results = "Taken"
    except:
        results = "Error"
    db.close()
    return results

def addUser(first,sec,email,username,password):
    db = pymysql.connect("localhost","Kiran","!winter@2018","BridgeBuilder")
    cursor = db.cursor()
    command = ("INSERT INTO User (Username,First_Name,Surname,Email,Password)    VALUES ('%s','%s','%s','%s','%s');"%(username,first,sec,email,password))
    try:
        cursor.execute(command)
        db.commit()
        error = ""
    except:
        db.rollback()
        error = "Error connecting to database"
    db.close()
    return error

def findUser(username,password):
    db = pymysql.connect("localhost","Kiran","!winter@2018","BridgeBuilder")
    cursor = db.cursor()
    command = ("SELECT * FROM User WHERE Username = '%s' and Password = '%s';"%(username,password))
    results = ""
    try:
        cursor.execute(command)
        if len(cursor.fetchall()) == 0:
            results = "Not"
    except:
        results = "Error"
    db.close()
    return results

def getUser_ID(username):
    db = pymysql.connect("localhost","Kiran","!winter@2018","BridgeBuilder")
    cursor = db.cursor()
    command = "SELECT User_ID FROM User WHERE Username = '%s';" %(username)
    ID = ""
    try:
        cursor.execute(command)
        result = cursor.fetchall()
        ID  = result[0][0]
    except:
        ID = ""
    db.close()
    return ID

def findBridge(name,User_ID):
    db = pymysql.connect("localhost","Kiran","!winter@2018","BridgeBuilder")
    cursor = db.cursor()
    command = "SELECT * FROM Bridges WHERE User_ID = '%s' AND Bridge_Name = '%s';" %(User_ID,name)
    results = ""
    try:
        cursor.execute(command)
        if len(cursor.fetchall()) > 0:
            results = "Taken"
    except:
        results = "Error"
    db.close()
    return results

def addBridge(name,adjacencyList,info):
    db = pymysql.connect("localhost","Kiran","!winter@2018","BridgeBuilder")
    cursor = db.cursor()
    command = ('INSERT INTO Bridges (User_ID,Bridge_Name,Date_Last_Edit,BridgeFile,Difficulty,Land_Type) VALUES ("%s","%s",CURDATE(),"%s","%s","%s");'%(info['User_ID'],name,adjacencyList,info['dif'],info['land']))
    try:
        cursor.execute(command)
        db.commit()
        error = ""
    except pymysql.Error as e:
#        print(e)
        db.rollback()
        error = "Error"
    db.close()
    return error

def getBridges(User_ID):
    db = pymysql.connect("localhost","Kiran","!winter@2018","BridgeBuilder")
    cursor = db.cursor()
    command = "SELECT Bridge_ID,Bridge_Name,DAYOFMONTH(Date_Last_Edit),MONTH(Date_Last_Edit),YEAR(Date_Last_Edit) FROM Bridges WHERE User_ID = '%s';" %(User_ID)
    results = ""
    try:
        cursor.execute(command)
        results = cursor.fetchall()
    except:
        results = "Error"
    db.close()
    return results

def deleteBridge(bridgeID):
    db = pymysql.connect("localhost","Kiran","!winter@2018","BridgeBuilder")
    cursor = db.cursor()
    command = ("DELETE FROM Bridges WHERE Bridge_ID = '%s'"%(bridgeID))
    try:
        cursor.execute(command)
        db.commit()
    except:
        db.rollback()
    db.close()

def getBridgeFile(bridgeID):
    db = pymysql.connect("localhost","Kiran","!winter@2018","BridgeBuilder")
    cursor = db.cursor()
    command = ("SELECT BridgeFile,Difficulty,Land_Type FROM Bridges WHERE Bridge_ID = '%s'"%(bridgeID))
    try:
        cursor.execute(command)
        results = cursor.fetchall()
    except:
        pass
    db.close()
    return results[0]

def updateBridge(bridgeID,adjacencyList):
    db = pymysql.connect("localhost","Kiran","!winter@2018","BridgeBuilder")
    cursor = db.cursor()
    command = ('UPDATE Bridges SET BridgeFile = "%s", Date_Last_Edit = CURDATE() WHERE Bridge_ID = "%s";'%(adjacencyList,bridgeID))
    try:
        cursor.execute(command)
        db.commit()
    except pymysql.Error as e:
        #print(e)
        db.rollback()

def getBridgeID(name,ID):
    db = pymysql.connect("localhost","Kiran","!winter@2018","BridgeBuilder")
    cursor = db.cursor()
    command = ("SELECT Bridge_ID FROM Bridges WHERE (User_ID = '%s' AND Bridge_Name = '%s')"%(ID,name))
    try:
        cursor.execute(command)
        results = cursor.fetchall()
    except pymysql.Error as e:
    #    print(e)
        pass
    return results[0][0]

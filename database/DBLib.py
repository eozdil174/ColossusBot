#Import the required database
import sqlite3 as sqldb
import sys
sys.path.append('C:\\Users\\eozdi\\Documents\\ColossusBot\\cogs')
from experienceManagement import experienceManagement

#Connect to the database. If the database doesn't exists if will be automatically created
connection = sqldb.connect('C:\\Users\\eozdi\\Documents\\ColossusBot\\database\\serverDatabase.db')

#Setting a cursor for sending commands to database
cursor = connection.cursor()

#Creating a database table or checking the database
cursor.execute('''CREATE TABLE IF NOT EXISTS Person (UserDiscriminator NOT NULL PRIMARY KEY ,UserName NOT NULL, UserCurrency, UserExp, UserLevel, isAdmin BOOLEAN FALSE )''')     #Executing the command. So the action will be applied to database
cursor.execute('''CREATE TABLE IF NOT EXISTS Roles (RoleName, RoleAvailable BOOLEAN)''')       #Adding the roles table to database

#######################################   USERBASE FUNCTIONS  #####################################################

def ifAdmin(userDisc):
    cursor.execute('SELECT isAdmin FROM Person WHERE UserDiscriminator=(?)', (userDisc,))
    isAdmin = cursor.fetchone()

    if isAdmin:
        return True
    else:
        return False

def getEntry(userDisc):
    cursor.execute('SELECT UserName FROM Person WHERE UserDiscriminator=(?)', (userDisc,))
    userName = cursor.fetchone()
    return userName

entryDiscriminators = []
def getEntries():
    entryDiscriminators.clear()
    entries = []

    for row in cursor.execute('SELECT * FROM Person'):
        entries.append(row)

    for uDisc in cursor.execute('SELECT UserDiscriminator FROM Person'):
        entryDiscriminators.append(str(uDisc)[2:6])


def saveEntry(userName, userDiscriminator, userCurrency, userExp):

    getEntries()

    if str(userDiscriminator) not in entryDiscriminators:
        cursor.execute("INSERT INTO Person(UserDiscriminator,UserName,UserCurrency,UserExp, UserLevel, isAdmin) VALUES (?,?,?,?,?,?)",(userDiscriminator, userName, 100, 1000, 1, False,))
        connection.commit()
        print("User " + userName +" saved to database")
    else:
        print("User " + userName + " exists. Passing the entry")
        pass


def deleteEntry(userDiscriminator):

    ans = input("The entry which has " + userDiscriminator + " Will be deleted. Are you sure ?( Write YES if you accept ) \n Answer: ")
    if ans == 'YES':

        cursor.execute("DELETE FROM Person WHERE UserDiscriminator = (?)", (userDiscriminator))
        connection.commit()
        print("Entry deleted with following number : " + userDiscriminator)


def getCookies(userDiscriminator):
    cursor.execute('SELECT UserCurrency FROM Person WHERE UserDiscriminator=(?)',(userDiscriminator,))
    cookies = cursor.fetchone()[0]
    return cookies


def giveCookies(donator, cookieVal, userDiscriminator):

    oldCurrency = getCookies(userDiscriminator)
    oldCurrency = int(oldCurrency)
    cookieVal = int(cookieVal)
    newCookieVal = oldCurrency + cookieVal

    cursor.execute('UPDATE Person SET UserCurrency=(?) WHERE UserDiscriminator=(?)',(newCookieVal, userDiscriminator))

    oldCurrency = getCookies(donator)
    oldCurrency = int(oldCurrency)
    cookieVal = int(cookieVal)
    newCurrency = oldCurrency - cookieVal
    cursor.execute('UPDATE Person SET UserCurrency=(?) WHERE UserDiscriminator=(?)',(newCurrency, donator))
    connection.commit()

############################################    EXPERIENCE SYSTEM FUNCTIONS  ####################################################

def getExp(userDiscriminator):
    cursor.execute('SELECT UserExp, UserLevel From Person WHERE UserDiscriminator=(?)',(userDiscriminator,)) #!!!! The comma is here to prevent function overload problem !!!!#
    userExp = cursor.fetchone()
    return userExp


def addExp(userDiscriminator, newExp):
    oldData = getExp(userDiscriminator)
    currentExp = float(newExp) + float(oldData[0])
    userLevel = int(oldData[1])

    if currentExp >= float(oldData[1]*1000):   #If userExp is bigger or equal to target exp (oldData[1] is userLevel)
        userLevel = int(oldData[1]) + 1
        cursor.execute('UPDATE Person SET UserExp=(?), UserLevel=(?) WHERE UserDiscriminator=(?)',(currentExp, userLevel, userDiscriminator))
        connection.commit()
        return True

    else:
        cursor.execute('UPDATE Person SET UserExp=(?), UserLevel=(?) WHERE UserDiscriminator=(?)',(currentExp, userLevel, userDiscriminator))
        connection.commit()
        return False


def removeExp(userDiscriminator, amount):
    currentExp = int(getUserExp(userDiscriminator)[0])
    newExp = currentExp - int(amount)
    cursor.execute('UPDATE Person SET UserExp=(?) WHERE UserDiscriminator=(?)', (newExp, userDiscriminator))
    connection.commit()

def getUserExp(userDiscriminator):
    cursor.execute('SELECT UserExp, UserLevel FROM Person WHERE UserDiscriminator=(?)',(userDiscriminator,))
    userData = cursor.fetchone()
    return userData

################################################    ROLE SYSTEM FUNCTIONS   #######################################################

def saveRoles(roles):
    for role in roles:
        cursor.execute("INSERT INTO Roles(RoleName, RoleAvailable) VALUES(?,?)",(str(role),roles[role]))


def getRoles():
    cursor.execute("SELECT RoleName FROM Roles WHERE RoleAvailable = 1")
    return cursor.fetchall()


def clearRoles():
    cursor.execute("DELETE FROM Roles")

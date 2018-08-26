#Import the required database
import sqlite3 as sqldb

#Connect to the database. If the database doesn't exists if will be automatically created
connection = sqldb.connect('C:\\Users\\eozdi\\Documents\\ColossusBot\\database\\serverDatabase.db')

#Setting a cursor for sending commands to database
cursor = connection.cursor()

#Creating a database table or checking the database
cursor.execute('''CREATE TABLE IF NOT EXISTS Person (UserDiscriminator NOT NULL PRIMARY KEY ,UserName NOT NULL, UserCurrency, UserExp, UserLevel, isAdmin BOOLEAN FALSE )''')     #Executing the command. So the action will be applied to database
cursor.execute('''CREATE TABLE IF NOT EXISTS Roles (RoleName, RoleAvailable BOOLEAN)''')       #Adding the roles table to database

entryDiscriminators = []
def getEntries():
    entryDiscriminators.clear()
    entries = []

    for row in cursor.execute('SELECT * FROM Person'):
        entries.append(row)

    for uDisc in cursor.execute('SELECT UserDiscriminator FROM Person'):
        entryDiscriminators.append(str(uDisc)[2:6])


def saveEntry(userName, userDiscriminator, userCurrency, userExp):
#Putting things to database TABLE
    getEntries()

    if str(userDiscriminator) not in entryDiscriminators:
        cursor.execute("INSERT INTO Person(UserDiscriminator,UserName,UserCurrency,UserExp, UserLevel, isAdmin) VALUES (?,?,?,?,?,?)",(userDiscriminator, userName, 100, 10,0,False,))
        connection.commit()
        print("User " + userName +" saved to database")
    else:
        print("User " + userName + " exists. Passing the entry")
        pass

#Reading from the database TABLE
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
    cursor.execute('SELECT UserExp From Person WHERE UserDiscriminator=(?)',(userDiscriminator,)) #!!!! The comma is here to prevent function overload problem !!!!#
    userExp = cursor.fetchone()
    return userExp

def addExp(userDiscriminator, newExp):
    oldExp = getExp(userDiscriminator)
    currentExp = newExp + oldExp[0]

    cursor.execute('UPDATE Person SET UserExp=(?) WHERE UserDiscriminator=(?)',(currentExp, userDiscriminator))
    connection.commit()


################################################    ROLE SYSTEM FUNCTIONS   #######################################################

def saveRoles(roles):
    for role in roles:
        cursor.execute("INSERT INTO Roles(RoleName, RoleAvailable) VALUES(?,?)",(str(role),roles[role]))

def getRoles():
    cursor.execute("SELECT RoleName FROM Roles WHERE RoleAvailable = 1")
    return cursor.fetchall()

def clearRoles():
    cursor.execute("DELETE FROM Roles")

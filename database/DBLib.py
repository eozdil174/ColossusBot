#Import the required database
import sqlite3 as sqldb

#Connect to the database. If the database doesn't exists if will be automatically created
connection = sqldb.connect('C:\\Users\\eozdi\\Documents\\ColossusBot\\database\\userBase.db')

#Setting a cursor for sending commands to database
cursor = connection.cursor()

#Creating a database table or checking the database
cursor.execute('''CREATE TABLE IF NOT EXISTS Person (UserNum INTEGER PRIMARY KEY AUTOINCREMENT ,UserName NOT NULL, UserDiscriminator NOT NULL, UserCurrency, UserExp)''')     #Executing the command. So the action will be applied to database
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
        cursor.execute("INSERT INTO Person(UserName,UserDiscriminator,UserCurrency,UserExp) VALUES (?,?,?,?)",(userName, userDiscriminator, 100, 10))
        connection.commit()
        print("User " + userName +" saved to database")
    else:
        print("User " + userName + " exists. Passing the entry")
        pass

#Reading from the database TABLE
def deleteEntry(userNum):

    ans = input("The entry which has " + userNum + " Will be deleted. Are you sure ?( Write YES if you accept ) \n Answer: ")
    if ans == 'YES':

        cursor.execute("DELETE FROM Person WHERE UserNum = (?)", (userNum))
        connection.commit()
        print("Entry deleted with following number : " + userNum)


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

def getExp(userDiscriminator):
    cursor.execute('SELECT UserExp From Person WHERE UserDiscriminator=(?)',(userDiscriminator,))
    userExp = cursor.fetchone()[0]
    return userExp

def addExp(userDiscriminator, newExp):
    cursor.execute('UPDATE Person SET UserExp=(?) WHERE UserDiscriminator=(?)',(newExp, userDiscriminator))
    connection.commit()

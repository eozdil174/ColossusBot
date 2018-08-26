import DBLib as db
exit = False

while exit != True:
    print ("\nCurrent database actions:\n-Add Entry = Adds a new entry to database\n-Delete Entry = Deletes an entry from the database\n-Show Entries = Shows the whole entries")
    answer = input("\nDatabase Action: ")

    if answer == 'Add Entry':
        uName = input("\nUser Name: ")
        uDiscriminator = input("\nUser Discriminator: ")
        uCurrency = input("\nUser Currency: ")
        msgCount = input("\nMessage Count: ")

        db.saveEntry(uName,uDiscriminator,uCurrency,msgCount)

    if answer == 'Delete Entry':
        uNum = input("\nUser Number: ")
        db.deleteEntry(uNum)

    if answer == 'len':
        message = input("\nMessage: ")
        print (len(message))

    if answer == 'userData':
        print(db.getUserData('9600'))


    
    if answer == 'Test Mode':
        db.addExp('9600', 120)
        print ("Done")
    if answer == 'Show Entries':

        print(db.getEntries())
    if answer == "Exit":
        exit = True

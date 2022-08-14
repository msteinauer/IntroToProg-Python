# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare variables and constants
objFileName = "ToDoFile.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, Load from ToDoFile.txt into a python Dictionary.
objFile = open(objFileName, "r")
for line in objFile:
    strData = line.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# Step 2 - Display a menu of choices to the user
while(True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # Add an extra line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue  # to show the menu
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Current Data in table:")
        # for dicRow in lstTable:
        #     print(dicRow)
        #Step 4a - Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue  # to show the menu
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        #Step 5a - Allow user to indicate which row to delete
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        for row in lstTable:
            task, priority = dict(row).values()
            if task == strKeyToRemove:
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
            #end if
        # end for loop
        #Step 5b - Update user on the status
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")

        #Step 5c - Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue  # to show the menu
    # Step 6 - Save tasks to the ToDoFile.txt file
    elif(strChoice == '4'):
        #Step 5a - Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        #Step 5b - Ask if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu
    elif (strChoice == '5'):
        break   # and Exit the program

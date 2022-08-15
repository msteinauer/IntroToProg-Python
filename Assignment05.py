# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# MSteinauer,8.8.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFileName = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
objFile = None  # An object that represents a file

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# File to List

objFile = open(objFileName, "r")
for row in objFile:
    lstRow = row.split(",")  # Returns a list!
    dicRow = {"Priority": lstRow[0],  "Task": lstRow[1].strip()}
    lstTable.append(dicRow)
    print(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""                                                                                                   
    Menu of Options                                                                                             
    1) Show current data                                                                                        
    2) Add a new Task.                                                                                          
    3) Remove the last task added.                                                                                 
    4) Save Data to File                                                                                        
    5) Exit Program                                                                                             
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5]: "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Priority"] + " " + row["Task"])
        print("*******************************************")  # Step 4 - Add a new item to the list/Table
        continue
        # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("The priority of the task and the task you would like to add to your list")
        strTask = input("Task to do: ")
        strPriority = input("Priority of the task: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable += [dicRow]
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        lstTable.remove(dicRow)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(objFileName, "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Priority"] + "," + dicRow["Task"] + "\n")
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exit the program.")
        break  # and Exit the program
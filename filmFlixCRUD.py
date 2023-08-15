"""This is a CRUD application for managing film records"""

import addFilms, deleteFilms, printAll, updateFilms

# function to read the respective menu files with their options
def menuFiles():
    with open("filmFlixCRUD.txt") as mainMenu:
        userMenu = mainMenu.read()
    return userMenu
    
def filmsMenu():

    options = 0 # create option variable and initialise it with integer value 0
    optionsList = ["1","2","3","4","5"] # create a list with string values
    # call/invoke the menuFiles function and assign/initialise with the userChoice variable
    userChoices = menuFiles()

    # while 0 not in ["1","2","3","4","5","6"] 
    while options not in optionsList: # execute the indented code
        print(userChoices)

        # re-assign the options variable with the input function(which has a default string data type)
        options = input("Enter an option from the choices above: ") # "1"/"2"

        # check to see if the reassigned options variable(value) is not in the optionsList(list) 
        if options not in optionsList:
            print(f"{options} is not a valid choice in the menu! ")
    return options

# create a boolean variable and assign with a True value 
mainProgram = True
while mainProgram: # same as While True
    
    mainMenu = filmsMenu() # assign filmsMenu function to the mainMenu variable
    #call/invoke the respective modules with their function

    if mainMenu == "1":
        addFilms.insert_data()
        # input("Press Enter to return to the main menu...") # add a pause after displaying the films to give the user a chance to read them
    elif mainMenu == "2":
        deleteFilms.delete_data()
    elif mainMenu == "3":
        updateFilms.update_data()
    elif mainMenu == "4":
        printAll.read_data()
    else:
        # reassign the maiProgram boolean variable with a False value
        mainProgram = False
        
    input("Press Enter to quit the app")
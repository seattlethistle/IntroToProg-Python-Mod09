# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# SDH,12.14.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
lstTable = []  # A list that acts as a 'table' of rows

# TODO: Import Modules
#SDH COPY THE IMPORT/TEST CODE FROM Listing12
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

#SDH THE FOLLOWING TEST CODE SHOULD PROBABLY BE IN THE TEST HARNESS...?
#SDH THEN DOLLAR OUT OUT THE TEST CODE BUT USE BITS OF IT LATER
# Test data module
# objP1 = Emp(1, "Bob", "Smith")
# objP2 = Emp(2, "Sue", "Jones")
# lstTable = [objP1, objP2]
# for row in lstTable:
#     print(row.to_string(), type(row))
# Test processing module
# Fp.save_data_to_file("EmployeeData.txt", lstTable)
# lstFileData = Fp.read_data_from_file("EmployeeData.txt")
# lstTable.clear()
# for line in lstFileData:
#     lstTable.append(Emp(line[0], line[1], line[2].strip()))
# for row in lstTable:
#     print(row.to_string(), type(row))
# Test IO classes
# Eio.print_menu_items()
# Eio.print_current_list_items(lstTable)
# print(Eio.input_employee_data())
# print(Eio.input_menu_options())

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
# objP1 = Emp(1, "Bob", "Smith")
# objP2 = Emp(2, "Sue", "Jones")
# lstTable = [objP1, objP2]
# Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
#SDH NO NEED TO PRINT THIS HERE
# for row in lstTable:
#     print(row.to_string(), type(row))

# Show user a menu of options
#Eio.print_menu_items()

#SDH COPY THE MENU CODE BELOW FROM ASSIGNMENT06 AND MODIFY THE NAMES

# Get user's menu option choice
while (True):
    Eio.print_menu_items()  # Shows menu
    strChoice = Eio.input_menu_options()  # Get menu option

    # Show user current data in the list of employee objects
    if strChoice == '1':  # Show current data
        Eio.print_current_list_items(lstTable)
        continue  # to show the menu

    # Let user add data to the list of employee objects
    elif strChoice == '2':  # Add a new Task
        lstTable.append(Eio.input_employee_data())
        continue  # to show the menu

    # let user save current data to file
    elif strChoice == '3':  # Save Data to File
        #Fp.save_data_to_file("EmployeeData.txt", lstTable)

        strChoice = Fp.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Fp.save_data_to_file("EmployeeData.txt", lstTable)
            Fp.input_press_to_continue(strChoice)
        else:
            Fp.input_press_to_continue("Save Cancelled!")

        continue  # to show the menu

    # Let user exit program
    elif strChoice == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit

# Main Body of Script  ---------------------------------------------------- #
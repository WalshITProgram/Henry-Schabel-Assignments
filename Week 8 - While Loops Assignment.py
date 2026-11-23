#Week 8 - While Loops Assignment

#Create an empty list to store employee dictionaries
employee_records = []

employee_count = 0

#Continue collecting employee information until 5 employees have been entered
while employee_count < 5:

    #Employee ID validation
    employee_id_ok = False

    while not employee_id_ok:
        employee_id = input("Please enter the Employee ID (7 digits or less): ")

        if employee_id:
            try:
                int(employee_id)
                if len(employee_id) <= 7 and employee_id.isdigit():
                    employee_id_ok = True
                else:
                    employee_id_ok = False
            except:
                employee_id_ok = False
        else:
            employee_id_ok = False

        if not employee_id_ok:
            print("Invalid Employee ID. Please enter a number with 7 or less digits.")


    #Employee Name validation
    employee_name_ok = False
    name_invalid_characters = "!\"@#$%^&*()_=+,<>/?;:[]{}\\"

    while not employee_name_ok:
        employee_name = input("Please enter the Employee Name: ")

        letter_count = 0

        if employee_name:
            for character in employee_name:
                if character.isalpha():
                    letter_count += 1

            if letter_count > len(employee_name) / 2:
                employee_name_ok = True

                for character in employee_name:
                    if character in name_invalid_characters:
                        employee_name_ok = False
            else:
                employee_name_ok = False

        if not employee_name_ok:
            print("Invalid Employee Name. Please enter a name containing primarily letters.")


    #Employee Email Address validation
    employee_email_ok = False
    email_invalid_characters = "!\"'#$%^&*()=+,<>/?;:[]{}\\"

    while not employee_email_ok:
        employee_email = input("Please enter the Employee Email Address: ")

        alphanumeric_count = 0

        if employee_email:
            for character in employee_email:
                if character.isalnum():
                    alphanumeric_count += 1

            if alphanumeric_count > len(employee_email) / 2:
                employee_email_ok = True

                for character in employee_email:
                    if character in email_invalid_characters:
                        employee_email_ok = False
            else:
                employee_email_ok = False

        if not employee_email_ok:
            print("Invalid Employee Email Address. Please try again.")


    #Employee Address validation
    employee_address_ok = False
    address_invalid_characters = "!\"'@$%^&*_=+<>?;:[]{}"

    while not employee_address_ok:
        employee_address = input("Please enter the Employee Address (or press Enter to skip): ")

        alphanumeric_count = 0

        #An address is optional
        if not employee_address:
            employee_address_ok = True
        else:
            for character in employee_address:
                if character.isalnum():
                    alphanumeric_count += 1

            if alphanumeric_count > len(employee_address) / 2:
                employee_address_ok = True

                for character in employee_address:
                    if character in address_invalid_characters:
                        employee_address_ok = False
            else:
                employee_address_ok = False

        if not employee_address_ok:
            print("Invalid Employee Address. Please try again.")


    #Create an employee dictionary and add it to the list
    employee_records.append({
        "employee_id": employee_id,
        "employee_name": employee_name,
        "employee_email": employee_email,
        "employee_address": employee_address
    })

    employee_count += 1

    #Ask whether the user wants to enter another employee
    if employee_count < 5:
        add_another_employee = input("Would you like to add another employee? (Y or N): ")

        if add_another_employee.upper() == "N":
            break


#Print the completed list of employee dictionaries
print("Employee Records:")
print(employee_records)
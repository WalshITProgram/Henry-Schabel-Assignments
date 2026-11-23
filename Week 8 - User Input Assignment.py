program_running = True

#Employee ID validation
employee_id = input("Please enter your Employee ID (7 digits or less): ")

employee_id_ok = False

if employee_id:
    try:
        int(employee_id)
        if len(employee_id) <= 7:
            employee_id_ok = True
        else:
            employee_id_ok = False
    except:
        employee_id_ok = False

if not employee_id_ok:
    print("Invalid Employee ID. The ID must be a number with 7 or less digits.")
    program_running = False


#Employee Name validation
if program_running:
    employee_name = input("Please enter your Employee Name: ")

    employee_name_ok = False
    letter_count = 0
    invalid_characters = '!\"@#$%^&*()_=+,<>/?;:[]{}\\'

    if employee_name:
        for character in employee_name:
            if character.isalpha():
                letter_count += 1

        if letter_count > len(employee_name) / 2:
            employee_name_ok = True

        for character in employee_name:
            if character in invalid_characters:
                employee_name_ok = False

    if not employee_name_ok:
        print("Invalid Employee Name.")
        program_running = False


#Employee Email Address validation
if program_running:
    employee_email = input("Please enter your Employee Email Address: ")

    employee_email_ok = False
    alphanumeric_count = 0
    invalid_characters = "!\"'# $%^&*()=+,<>/?;:[]{}\\"
    invalid_characters = invalid_characters.replace(" ", "")

    if employee_email:
        for character in employee_email:
            if character.isalnum():
                alphanumeric_count += 1

        if alphanumeric_count > len(employee_email) / 2:
            employee_email_ok = True

        for character in employee_email:
            if character in invalid_characters:
                employee_email_ok = False

    if not employee_email_ok:
        print("Invalid Employee Email Address.")
        program_running = False


#Employee Address validation
if program_running:
    employee_address = input("Please enter your Employee Address (or press Enter to skip): ")

    employee_address_ok = True
    alphanumeric_count = 0
    invalid_characters = "!\"'@$%^&*_=+<>?;:[]{}"

    if employee_address:
        for character in employee_address:
            if character.isalnum():
                alphanumeric_count += 1

        if alphanumeric_count <= len(employee_address) / 2:
            employee_address_ok = False

        for character in employee_address:
            if character in invalid_characters:
                employee_address_ok = False

    if not employee_address_ok:
        print("Invalid Employee Address.")
        program_running = False


#Display the employee information if all entries are valid
if program_running:
    print("Hello, " + employee_name + ". Your Employee ID is " + employee_id + ", and your email address is " + employee_email + ".")

    if employee_address:
        print("Your address is " + employee_address)
    else:
        print("You did not provide an address.")
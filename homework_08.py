login = input('Please enter your Login (letters only) >>> ')
password = input('Please enter your Password (letters and numbers only)  >>> ')
confirm_password = input('Please confirm your password (letters and numbers only) >>> ')

login_success_template = (f'Welcome {login}, you have successfully logged in.')
password_match_false = (f'{login} your passwords do not match, please try again.')
login_requirements_met = login.isalpha()
password_syntax_met = password.isalnum() and confirm_password.isalnum()
password_requirements_met = (password == confirm_password)

if password_syntax_met and login_requirements_met:
    if password_requirements_met:
        print(login_success_template)
        print('You have been logged out.')
        if password_syntax_met:
            if password_requirements_met:
                login_repeat = input('Please re-enter your Login (letters and numbers only)  >>> ')
                password_repeat = input('Please confirm your password (letters and numbers only) >>> ')
                if login_repeat == login and password_repeat == password:
                    print(login_success_template)
                else:
                    print(password_match_false)
            else:
                print(password_match_false)
        else:
            print(f'Please enter proper login or password!')
    else:
        print(password_match_false)

else:
    print(f'Please enter proper login or password!')

login = input('Please enter your Login (letters only) >>> ')
password = input('Please enter your Password (letters and numbers only)  >>> ')
confirm_password = input('Please confirm your password (letters and numbers only) >>> ')
login_requirements_met = login.isalpha()
password_syntax_met = password.isalnum() and confirm_password.isalnum()
password_requirements_met = (password == confirm_password)

if password_syntax_met and login_requirements_met:
    if password_requirements_met:
        print(f'Welcome {login}, you have successfully logged in.')
        print('You have been logged out.')
        if password_syntax_met:
            if password_requirements_met:
                l=input('Please re-enter your Login (letters and numbers only)  >>> ')
                p=input('Please confirm your password (letters and numbers only) >>> ')
                if l == login and p == password:
                    print(f'Welcome {login}, you have successfully logged in.')
                else:
                    print(f'{login} your passwords do not match, please try again.')
            else:
                print(f'{login} your passwords do not match, please try again.')
        else:
            print(f'Please enter proper login or password!')
    else:
        print(f'{login} your passwords do not match, please try again.')

else:
    print(f'Please enter proper login or password!')






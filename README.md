# Password Strength Checker (Python)

## Overview
This project is a simple Python-based Password Strength Checker developed for MediSure Health Services as part of a cybersecurity improvement initiative. The script evaluates the strength of a user-entered password based on commonly accepted security criteria and provides clear, actionable tips for improvement.

The program supports:
- Length checking  
- Lowercase, uppercase, digit, and symbol detection  
- Weak / OK / Strong rating  
- Helpful security tips  
- Continuous testing in a loop  
- Graceful handling of empty inputs  
- Exit command for convenience  

This tool is intended for learning and demonstration purposes only. It should not be used to test real user passwords.

---

## Features
- ✔ Uses only Python built-in functions (no external libraries required)  
- ✔ Simple scoring system (0–5 points)  
- ✔ Provides clear strength ratings (Weak / OK / Strong)  
- ✔ Displays up to 2 improvement tips  
- ✔ Allows repeated testing without restarting  
- ✔ Exits safely when the user types `"exit"`  
- ✔ Clean, modular, and beginner-friendly code  

---

## Requirements
- Python 3.10 or later  
- VS Code (recommended, but any editor works)  

No third-party modules are required.

---

## How to Run the Program

1. Verify Python is installed:

python --version

2. Save the script as:

password_checker.py

3. Open a terminal in the script's folder.

4. Run the program:
python password_checker.py

or:
python3 password_checker.py


5. When prompted:
- Enter a password to test  
- View the strength rating  
- Read suggestions to improve  
- Type **exit** to quit the program  

---

## Example Output
Enter your password: Lily@1234

Password Rating: Strong
Great job! Your password meets all security requirements.

Type another password or type 'exit' to quit.

---

## File Structure
PasswordChecker/
 -password_checker.py # Main program
 -README.md # Instructions and documentation
 
---

## Notes
- This script does not store or transmit any passwords.  
- It is designed for educational use to demonstrate secure coding practices.  
- The code follows clean, modular design to improve readability and maintainability.



# Password Strength Checker (CLI)

## Overview

This project is a command-line password strength checker built with Python.  
It helps users evaluate how secure a password is using common security best practices
such as length, character variety, and pattern detection.

The tool provides:
- A numeric security score
- A visual strength bar
- Clear improvement tips
- Input validation for better user experience

This project was built as part of my learning and practice in Python, security
fundamentals, and clean CLI application design.

---

## Features

- Validates password strength based on:
  - Minimum length
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters
- Detects common weak patterns:
  - Common passwords (e.g. `password`, `123456`)
  - Sequential numbers (e.g. `123`)
  - Repeated characters (e.g. `aaa`)
- Displays:
  - Score out of 5
  - Visual strength bar (`[#----]`)
  - Clear improvement tips
- Handles invalid input gracefully:
  - Empty input
  - Overly long input
  - Accidental file path pastes

---

## Example Output

Enter password to check (or 'exit' to quit): lily@123

ANALYSIS RESULTS:
Security Score: 4/5
Rating: [####-] ⭐⭐⭐⭐ [STRONG]

IMPROVEMENT TIPS:
[!] Add uppercase letters (A-Z)
[!] Avoid sequential numbers (e.g., '123')

---

## Technologies Used

- Python 3
- Python Standard Library (`string`)
- Command Line Interface (CLI)

---

## Project Structure

PasswordChecker/

 - password_checker.py
 - README.md

---

## How to Run

1. Ensure Python 3 is installed
2. Open Command Prompt or Terminal
3. Navigate to the project folder
4. Run:

```bash
python password_checker.py



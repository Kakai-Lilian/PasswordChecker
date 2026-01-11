import string

# =========================
# Configuration
# =========================
MIN_LENGTH = 8
MAX_LENGTH = 64
REQUIREMENTS = {
    "length": True,
    "lowercase": True,
    "uppercase": True,
    "digits": True,
    "symbols": True
}

COMMON_PASSWORDS = {"password", "123456", "qwerty", "letmein", "admin"}

# =========================
# Functions
# =========================

def get_password():
    """Prompt the user for input and handle exit or empty input gracefully."""
    try:
        return input("\nEnter password to check (or 'exit' to quit): ").strip()
    except EOFError:
        return "exit"


def validate_input(password):
    """Check if input is valid (not file path, not too long)."""
    if len(password) > MAX_LENGTH:
        return False, f"Password too long. Max {MAX_LENGTH} characters."
    if "/" in password or "\\" in password or ":" in password:
        return False, "Invalid characters in password (slashes or colon)."
    if not password:
        return False, "Password cannot be empty."
    return True, ""


def check_strength(password):
    """Evaluate password strength and return score and feedback."""
    score = 0
    feedback = []

    # Length check
    if REQUIREMENTS["length"]:
        if len(password) >= MIN_LENGTH:
            score += 1
        else:
            feedback.append(f"Use at least {MIN_LENGTH} characters")

    # Lowercase
    if REQUIREMENTS["lowercase"]:
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Add lowercase letters (a-z)")

    # Uppercase
    if REQUIREMENTS["uppercase"]:
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Add uppercase letters (A-Z)")

    # Digits
    if REQUIREMENTS["digits"]:
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Add numeric digits (0-9)")

    # Symbols
    if REQUIREMENTS["symbols"]:
        if any(c in string.punctuation for c in password):
            score += 1
        else:
            feedback.append("Add special symbols (!@#$ etc.)")

    # Common passwords
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("Avoid common passwords (e.g., 'password', '123456')")
        score = max(score - 1, 0)

    # Check repeated/sequential characters
    feedback.extend(check_sequences(password))

    return score, feedback


def check_sequences(password):
    """Detect repeated characters or sequential numbers."""
    tips = []

    # Repeated characters (aaa, 111)
    for i in range(len(password)-2):
        if password[i] == password[i+1] == password[i+2]:
            tips.append("Avoid repeated characters (e.g., 'aaa')")
            break

    # Numeric sequences (123, 234)
    for i in range(len(password)-2):
        if password[i:i+3].isdigit():
            nums = list(map(int, password[i:i+3]))
            if nums[0]+1 == nums[1] and nums[1]+1 == nums[2]:
                tips.append("Avoid sequential numbers (e.g., '123')")
                break

    return tips


def get_rating(score):
    """Return colored rating + visual bar for password strength."""
    bar = "[" + "#"*score + "-"*(5-score) + "]"
    if score >= 5:
        return f"\033[92m{bar} ⭐⭐⭐⭐⭐ [EXCELLENT]\033[0m"
    elif score == 4:
        return f"\033[92m{bar} ⭐⭐⭐⭐ [STRONG]\033[0m"
    elif score == 3:
        return f"\033[93m{bar} ⭐⭐⭐ [GOOD]\033[0m"
    elif score == 2:
        return f"\033[91m{bar} ⭐⭐ [WEAK]\033[0m"
    else:
        return f"\033[91m{bar} ⭐ [VERY WEAK]\033[0m"


def main():
    """Main CLI loop for password strength testing."""
    # Sleek title
    print("\n=== ISP NETWORK SECURITY TOOL ===\n")

    while True:
        password = get_password()
        if password.lower() == "exit":
            print("\nExiting Secure Session. Goodbye!\n")
            break

        # Input validation
        valid, msg = validate_input(password)
        if not valid:
            print(f">> Error: {msg}")
            continue

        # Check password
        score, issues = check_strength(password)
        rating = get_rating(score)

        # Display results with clean spacing
        print("\n--- Analysis Results ---")
        print(f"Security Score: {score}/5")
        print(f"Rating: {rating}")

        if issues:
            print("\nImprovement Tips:")
            for issue in issues:
                print(f" [!] {issue}")
        else:
            print("\nSUCCESS: This password meets all security standards!")

        print("\n" + "-"*40 + "\n")


if __name__ == "__main__":
    main()


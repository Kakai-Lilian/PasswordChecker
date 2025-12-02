import string

MIN_LENGTH=8

def get_password():
    
    """Ask the user for a password. Return None if the input is empty."""
    
    password = input("Enter your password: ").strip()
    if password == "":
        print("Password input cannot be empty. Please try again...")
        return None
    return password

def has_lowercase(password):
    """Return True if password has at least one lowercase letter."""
    return any(char.islower() for char in password)

def has_uppercase(password):
    """Return True if password has at least one uppercase letter."""
    return any(char.isupper() for char in password)

def has_digit(password):
    """Return True if password has at least one number."""
    return any(char.isdigit() for char in password)

def has_symbol(password):
    """Return True if password has at least one symbol."""
    return any(char in string.punctuation for char in password)


def score_password(password):

    """
    Return a score (0-5) and a list of improvement tips
    based on password strength criteria.
    """
    score = 0
    tips = []

    if len(password) >= MIN_LENGTH:
        score += 1
    else:
        tips.append(f"Use at least {MIN_LENGTH} characters.")

    if has_lowercase(password):
        score += 1
    else:
        tips.append("Add lowercase letters (a-z).")

    if has_uppercase(password):
        score += 1
    else:
        tips.append("Add uppercase letters (A-Z).")

    if has_digit(password):
        score += 1
    else:
        tips.append("Add numbers (0-9).")

    if has_symbol(password):
        score += 1
    else:
        tips.append("Add symbols (!@#$ etc).")

    return score, tips

def password_rating(score):
    """Convert numeric score into a rating label."""
    if score <= 1:
        return "Weak"
    elif score <= 3:
        return "OK"
    else:
        return "Strong"


def main():
    """Main program loop for testing password strength."""
    while True:
        password = get_password()

        if password is None:
            continue  # ask again

        if password.lower() == "exit":
            print("Goodbye!")
            break  # stop the loop

        score, tips = score_password(password)
        rating = password_rating(score)

        print(f"\nPassword Rating: {rating}")

        # Add success message for strong passwords
        if rating == "Strong":
            print("Great job! Your password meets all security requirements.")

        if tips:
            print("Tips to improve:")
            for tip in tips[:2]:
                print(f"- {tip}")

        print("\nType another password or type 'exit' to quit.\n")



if __name__ == "__main__":
    main()



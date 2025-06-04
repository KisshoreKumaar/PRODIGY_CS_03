import re

def check_password_strength(password):
    feedback = []
    score = 0

    # Criteria
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))

    # Scoring logic
    if length >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if has_upper:
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")

    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z).")

    if has_digit:
        score += 1
    else:
        feedback.append("Add digits (0-9).")

    if has_special:
        score += 1
    else:
        feedback.append("Add special characters (e.g., !, @, #, $, etc.).")

    # Determine strength
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    print("🔐 Password Strength Checker")
    password = input("Enter a password to check: ").strip()

    strength, feedback = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f" - {suggestion}")
    else:
        print("Great job! Your password is strong.")

if __name__ == "__main__":
    main()

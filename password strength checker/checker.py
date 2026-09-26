import string


def check_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Minimum 8 characters required.")

    # Check uppercase letter
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    # Check lowercase letter
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    # Check number
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add a number.")

    # Check special character
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add a special character.")

    # Decide strength
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, score, feedback
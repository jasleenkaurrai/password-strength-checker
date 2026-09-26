def validate_password(password):
    if password == "":
        return False, "Password cannot be empty."

    if " " in password:
        return False, "Spaces are not allowed."

    return True, "Valid Password"
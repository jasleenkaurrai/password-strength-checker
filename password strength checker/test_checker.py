from checker import check_strength

print("===== PASSWORD CHECKER TESTING =====\n")

# Test 1
strength, score, feedback = check_strength("Hello123@")

print("Test 1 - Very Strong Password")
print("Password: Hello123@")
print("Score:", score)
print("Strength:", strength)

assert score == 5
assert strength == "Very Strong"

print("PASS\n")


# Test 2
strength, score, feedback = check_strength("Hello123")

print("Test 2 - Strong Password")
print("Password: Hello123")
print("Score:", score)
print("Strength:", strength)

assert score == 4
assert strength == "Strong"

print("PASS\n")


# Test 3
strength, score, feedback = check_strength("hello")

print("Test 3 - Very Weak Password")
print("Password: hello")
print("Score:", score)
print("Strength:", strength)

assert score == 1
assert strength == "Very Weak"

print("PASS\n")


# Test 4
strength, score, feedback = check_strength("hello123@")

assert "Add an uppercase letter." in feedback

print("Test 4 - Missing Uppercase: PASS\n")


# Test 5
strength, score, feedback = check_strength("HelloWorld@")

assert "Add a number." in feedback

print("Test 5 - Missing Number: PASS\n")


# Test 6
strength, score, feedback = check_strength("Hello123")

assert "Add a special character." in feedback

print("Test 6 - Missing Special Character: PASS\n")


print("====================================")
print("ALL TESTS PASSED SUCCESSFULLY!")
print("====================================")
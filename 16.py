# Task: Check if a specific word (e.g., "error") exists in the file.
keyword = "error"
with open("mynotes.txt", "r") as file:
    content = file.read()
    if keyword in content:
        print(f"The word '{keyword}' was found in the file.")
    else:
        print(f"The word '{keyword}' was not found.")

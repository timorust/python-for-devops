# Task: Print only the first 5 lines of a file.
with open("mynotes.txt", "r") as file:
    for i in range(6):
        print(file.readline().strip())

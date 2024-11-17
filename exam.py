# Step 1: Write to the file (overwrite mode)
with open('mynotes.txt', 'w') as file:
    file.write("This is my first note.\n")

# Display the content after overwriting
with open('mynotes.txt', 'r') as file:
    print("After Step 1:\n", file.read())


# Step 2: Append another note
with open('mynotes.txt', 'a') as file:
    file.write("This is my second note.\n")

# Display the content after appending
with open('mynotes.txt', 'r') as file:
    print("After Step 2:\n", file.read())


# Step 3: Overwrite the file with a new note
with open('mynotes.txt', 'w') as file:
    file.write("This is my new note, replacing everything.\n")

# Display the content after overwriting again
with open('mynotes.txt', 'r') as file:
    print("After Step 3:\n", file.read())

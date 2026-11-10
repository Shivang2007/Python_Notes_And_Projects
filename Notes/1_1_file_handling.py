
# ------------------------------------------------------------
# FILE HANDLING
# ------------------------------------------------------------

# Modes:
# r = Read
# w = Write (overwrites existing content)
# a = Append
# x = Create a new file
# r+ = Read and write

# Writing into a file
with open("notes.txt", "w") as file:
    file.write("Learning Python")

# Reading a file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# Appending data
with open("notes.txt", "a") as file:
    file.write("\nPython is interesting!")


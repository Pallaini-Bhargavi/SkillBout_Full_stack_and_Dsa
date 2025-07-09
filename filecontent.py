filename = "sample.txt"

with open(filename, "w") as file:
    file.write("This is the first line.\n")
    file.write("Writing to the file using 'with' statement.\n")


with open(filename, "a") as file:
    file.write("This line is appended.\n")
    file.write("Appending more content to the file.\n")


with open(filename, "r") as file:
    content = file.read()
    print("File content:")
    print(content)

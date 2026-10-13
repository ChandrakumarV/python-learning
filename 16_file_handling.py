# file = open('filename.txt', 'mode')

try:
    file = open("note.txt", "r")
    print(file)
    print("Filename:", file.name)
    print("Mode:", file.mode)

    content = file.read()
    print(content)

    print("Is Closed?", file.closed)
    file.close()
    print("Is Closed?", file.closed)

    print('-----------')

except FileNotFoundError:
    print("File not found")


# Using with Statement
# Instead of manually opening and closing the file, you can use the with statement, which automatically handles closing. This reduces the risk of file corruption and resource leakage.


with open("note.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")

print("File written successfully")

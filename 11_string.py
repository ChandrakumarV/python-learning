# single ('...') or double ("...")
a = 'GFG'
b = "GeeksForGeeks"
print(a)
print(b)

# Multi-line Strings ('''...''' ) or ( """...""")
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)


# Accessing Characters in String (Positive indices/negative indices)
s = "ABCDEF"
print(s[0])
print(s[-1])


# String Slicing
s = "ABCDEF"
print(s[1:4])
print(s[:3])
print(s[3:])
print(s[::-1])

# Looping Through Strings
s = "ABCDEF"
for char in s:
    print(char)

# String Immutability
s = "aBCDEF"
s = "A" + s[1:]
print(s)


# Deleting a String
s = "ABC"
del s


# Updating a String
s = "ABCD EF"
s1 = "H" + s[1:]
s2 = s.replace("ABC", "abc")

print(s1)
print(s2)


# Common String Methods

s = "GeeksforGeeks"
print(len(s))


s = "Hello World"
print(s.upper())
print(s.lower())


s = "   ABC   "
print(s.strip())

s = "Python is fun"
print(s.replace("fun", "awesome"))


# Concatenating and Repeating

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)


s = "Hello "
print(s * 3)


# Formatting Strings

name = "Jake"
age = 22
print(f"Name: {name}, Age: {age}")


s = "My name is {} and I am {} years old.".format("Emily", 22)
print(s)


# String Membership Testing
s = "GeeksforGeeks"
print("Geeks" in s)
print("GfG" in s)

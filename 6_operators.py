# Arithmetic Operators

a = 21
b = 4

print("Addition         :", a + b)
print("Subtraction      :", a - b)
print("Multiplication   :", a * b)
print("Division         :", a / b)
print("Floor Division   :", a // b)
print("Modulus          :", a % b)
print("Exponentiation   :", a ** b)


# Comparison Operators

a = 13
b = 33

print("Greater than     :", a > b)
print("Less than        :", a < b)
print("Equal to         :", a == b)
print("Not equal to     :", a != b)
print("Greater/equal    :", a >= b)
print("Less/equal       :", a <= b)


# Logical Operators

a = True
b = False

print("Logical AND      :", a and b)
print("Logical OR       :", a or b)
print("Logical NOT      :", not a)


# Bitwise Operators

a = 10
b = 4

print("Bitwise AND      :", a & b)
print("Bitwise OR       :", a | b)
print("Bitwise NOT      :", ~a)
print("Bitwise XOR      :", a ^ b)
print("Right Shift      :", a >> 2)
print("Left Shift       :", a << 2)


# Assignment Operators

a = 10

a += 5
print("Add and Assign   :", a)

a -= 2
print("Subtract & Assign:", a)

a *= 3
print("Multiply & Assign:", a)

a /= 2
print("Divide & Assign  :", a)

a //= 2
print("Floor & Assign   :", a)

a %= 2
print("Modulus & Assign :", a)

a **= 2
print("Exponent & Assign:", a)


# Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("Identity is      :", a is b)
print("Identity is not  :", a is not c)


# Membership Operators

a = [10, 20, 30, 40]

print("Membership in    :", 20 in a)
print("Not in           :", 50 not in a)

# Ternary Operator

a, b = 10, 20
min = a if a < b else b

print("Ternary Operato  :", min)
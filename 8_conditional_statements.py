
# If Statement -------

age = 20
if age >= 18:
    print("Eligible to vote.")

# Short Hand - Single line
age = 19
if age > 18: print("Eligible to Vote.")


# If else Statement ------

age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")


# If-elif-else Statement -------

age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

# Nested if-else Statement --------

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")


# Conditional Expression (Ternary Operator) ----------
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)


# Match-Case Statement ------------

number = 2

match number:
    case 1:
        print("One")
    case 2 | 3: # multiple match
        print("Two or Three")
    case _: # default
        print("Other number")
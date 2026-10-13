n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")

# -------

try:
    n = 0
    res = 100 / n

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Enter a valid number!")

else:
    print("Result is", res)

finally:
    print("Execution complete.")

# ----------


def test():
    try:
        d = int(input("Enter Number : "))
    except Exception as e:
        print(str(e))
    else:
        print(d)
    finally:
        print("Execution completed")


test()

# 1. Specific Exceptions

try:
    # This will cause ValueError
    x = int("str")
    inv = 1 / x   # Inverse calculation

except ValueError:
    print("Not Valid!")

except ZeroDivisionError:
    print("Zero has no inverse!")


# 2. Multiple Exceptions

a = ["10", "twenty", 30]
try:
    # 'twenty' cannot be converted to int
    total = int(a[0]) + int(a[1])

except (ValueError, TypeError) as e:
    print("Error", e)

except IndexError:
    print("Index out of range.")

# 3. Catch-All Handlers and Their Risks

try:
    # Risky operation: dividing string by number
    res = "100" / 20

except ArithmeticError:
    print("Arithmetic problem.")

except:
    print("Something went wrong!")

# 4. Raise an Exception


def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")


try:
    set(-5)
except ValueError as e:
    print(e)

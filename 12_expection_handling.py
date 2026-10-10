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

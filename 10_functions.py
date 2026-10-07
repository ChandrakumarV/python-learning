# Named argument -----------
def student(fname, lname):
    print(fname, lname)


student("Geeks", "Practice")
student(fname="Geeks", lname="Practice")
student(lname="Practice", fname="Geeks")


# pass by reference ----------
def myFun(x):
    x[0] = 20


b = [10, 11, 12, 13]
myFun(b)
print(b[0])


# pass by value --------
def myFun2(x):
    x = 20


a = 10
myFun2(a)
print(a)

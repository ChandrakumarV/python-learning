# Scope of variable

a = 1
  
# Uses global because there is no local 'a' 
def f(): 
    print('Inside f() : ', a)
  
# Variable 'a' is redefined as a local 
def g():     
    a = 2
    print('Inside g() : ', a)
  
# Uses global keyword to modify global 'a' 
def h():     
    global a 
    a = 3
    print('Inside h() : ', a) 
  
# Global scope 
print('global : ', a)
f() 
print('global : ', a) 
g() 
print('global : ', a)
h() 
print('global : ', a)

# If you assign a variable anywhere inside a function, Python treats that variable as local throughout that function (unless you explicitly use global/nonlocal).

# --------------

def f():
    print(s)

    # This program will NOT show error
    # if we comment below line.
    s = "Me too."

    print(s)
	

# Global scope
s = "I love Geeksforgeeks"
f()
print(s)
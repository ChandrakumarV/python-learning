
# Python variables store references to objects, not the actual values 

x = 1
y=x
y=10

print(x) #1
print(y) #10


# Initially, both x and y reference the object 1.
# After y = 10, y references a new object 10 while x still references 1, so changing y does not affect x
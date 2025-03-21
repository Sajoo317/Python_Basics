# Tuple is immutable meaning value cannot be changed
a = (1,2,3,4,5) # This is a tuple and it is written this way
print(type(a))
b = () # This is an empty tuple
c = (1) # Python will consider this as an integer and not tuple
d = (1,) # This is a tuple containing only one element
e = (1,34,'sajeel', True, 10.23) # This is also a tuple with multiple datatypes
print(type(b))
print(type(c))
print(type(d))
print(e)
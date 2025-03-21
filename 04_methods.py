
a = {3,233,134,54,2}
b = {4,5,22,11,3}
print(a, type(a))
a.add(223) # this adds an element in the set 
print(a)
# union()   | symbol
# intersection()    & symbol
# difference()     - symbol

print("Union is: ", a.union(b))
print("Intersection is: ", a&b)


marks = {"Sajeel": 88, 
         "Nabeel": 77, 
         "faizan": 99 }

# print(marks.items()) # returns a list of keys,values in the form of tuple

# print(marks.keys()) # Gives a list containing only the keys of dictionary i.e left of :

# marks.update({"Sajeel": 99}) # uodates the given key and its value

# print(marks)

print(marks.get("Sajeel")) # Gives the value of the key
print(marks["Sajeel"]) # Gives value of the key 

# print(marks.get("Sajeel2")) # it gives None as there is no such key in the dict
# print(marks["Sajeel2"]) # this will give key error
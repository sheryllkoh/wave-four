def reverseLookup(data, value):
    keys = []
    
    for key in data:
        if data[key] == value:  
          keys.append(key)
    return keys 

    
student = {"sheryl" : "name", "sixteen" : "age", "bio" : "course", "math" : "course"}

onekey = reverseLookup(student, "name")

multiplekeys = reverseLookup(student, "course")

nokeys = reverseLookup(student, "phone")

print(multiplekeys)
print(onekey)
print(nokeys)

 
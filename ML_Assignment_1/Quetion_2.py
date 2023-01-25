# Create an empty dictionary called dog and Add name, color, breed, legs, age to the dog dictionary done
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Goldey"
dog["color"] = "Dark Golden"
dog["breed"] = "Golden Retriever"
dog["legs"] = 4
dog["age"] = 3
print(dog)
# Create a student dictionary and add first_name, last_name, gender,
# age, marital status, skills, country, city and address as keys for the dictionary done
student = {'first_name': ' Jethin Sai ',
           'last_name': ' Chilukuri',
           'gender': ' Male', 'age': ' 22 ',
           'marital_status': ' Single', 'skills': ['python'],  # we used sq brackets for list
           'country': ' India ', 'city': ' Gudivada ',
           'address': ' Flat no 118 B-block By pass road '}
# To get length of the dictionary we used len function
print("Length of student dictionary:", len(student))

S = student["skills"]  # Here we assigned student["skills"] to S and used type function to get the class
print("Data type of skills:", type(S))
student["skills"].append("C++")  # Here we use append function to add additional vales to List
student["skills"].append("Java")
K = list(student.keys())
print("Dictionary keys:", K)
v = list(student.values())
print("Dictionary values:", v)

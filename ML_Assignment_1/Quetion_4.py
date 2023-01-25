it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} #Given
A = {19, 22, 24, 20, 25, 26} #Given
B = {19, 22, 20, 25, 26, 24, 28, 27} #Given
age = [22, 19, 24, 25, 26, 24, 25, 24] #Given
print("The length of the set it_companies is",len(it_companies)) # we used len funtion to count
it_companies.add('Twitter') # we used add for single element for a set at a time
it_companies.update({"Samsung","Cognizant"}) # Here we use update funtion to add more than one
it_companies.remove("Cognizant") # Here we use removie funtion to remove Cognizant from the dischonery

#  What is the difference between remove and discard
# Remove (removies first element in the set) and discard methods: remove the specified item from the set –
# The item that should be removed is passed to both methods as an argument
# – Behave differently when the specified item is not found in the set
# To join A and B we used union method
C = A.union(B)
print(f"The set after joining A and B is {C}.")
# To find  A intersection B we used intersection
print(f"The intersection of A and B is {A.intersection(B)}.")
# Is A subset of B
print(f"Is A subset of B: {A.issubset(B)}")
# Are A and B disjoint sets
print(f"Are A and B disjoint sets: {A.isdisjoint(B)}")
# Join A with B and B with A
print(f"Join A with B and B with A {C} and {B.union(A)}")
print(f"The symmetric difference : {A.symmetric_difference(B)} ")
# Here to delete the sets completely we used del funtion
del it_companies
del A
del B
# Converting the ages to a set
ages = set(age)
# Compare the length of the list and the set
print("The length of the list age is ",len(age))
print("The length of the set ages is ",len(ages))

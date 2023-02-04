x = [23, 'Python', 23.98] # Given Input
y = [] # We created a empty list for the data type
for i in range(0,len(x)): # For loop starts from 0 to length of list x
    y.append(type(x[i])) # we us append funtion to add data type to list y
print(x)
print(y)
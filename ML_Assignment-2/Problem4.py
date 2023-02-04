Sample_List=[1,2,3,3,3,3,4,5] # Given list
Unique_List=[] # Created a empty list to store unique items
for i in Sample_List:
    if i not in Unique_List: # not in to remove the repeated elementes
        Unique_List.append(i) # Used append funtion to add to uniqe list
print(Unique_List)

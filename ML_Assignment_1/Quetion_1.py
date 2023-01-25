ages = [19,22,19,24,20,25,26,24,25,24]#Given
ages.sort() #we sort to arrange the values in assending order
Min_Age= ages[0]#Minimum Age
Max_Age= ages[-1]#Maximum Age
print("Min_Agea = ",Min_Age)#print minimum age
print("Max_Age = ",Max_Age)#print maximun age
ages.append(Min_Age)#Adding the minimum age to ages
ages.append(Max_Age)#Adding the Maximum age to ages
if len(ages) % 2 == 0:#using if state ment of even number of length to find Median
    Median_Age =(ages[int(len(ages)/2)] + ages[int(len(ages)/2) + 1]) / 2
else:#using else for odd number of element in ages to find Median
    Median_Age =ages[int(len(ages)/2)]
print("The Median Age = ",Median_Age)  
Avrage_Age = sum(ages)/len(ages)
print("The Average Age =",Avrage_Age)
Range_of_Ages= (Max_Age-Min_Age)
print("The Range of Ages =",Range_of_Ages)





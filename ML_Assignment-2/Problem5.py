Input_String='The quick Brow Fox' # Given
upper_case=0
lower_case=0
for i in Input_String:
    if(i.isupper()): # Here we used upper case function for capital letters
        upper_case+=1
    else:
        if(i.islower()): # Here used islowe function for non capital letters
            lower_case+=1
print("No. of Upper-case characters: "+str(upper_case))
print("No. of Lower-case characters: "+str(lower_case))
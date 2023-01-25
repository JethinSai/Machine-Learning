N = int(input("Enter number of students: "))
w_lbs = [] # According to the quation we need to us list for lbs and kgs
w_kgs = []

for i in range(N):
    w = float(input("Enter weight in pounds for student {}: ".format(i+1))) # Here it asks for
    w_lbs.append(w) # Here we use addend to add to lists
    w_in_kg = w * 0.453592 # Here we use addend to store weight in kg to list w_kgs
    w_kgs.append(w_in_kg)

print("Weights in pounds:", w_lbs)
print("Weights in kilograms:", w_kgs)

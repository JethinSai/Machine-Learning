# To get the output i decide to divide the input two triangles parts
for a in range(0, 6):  # First half to increase the numbers to 5th row
    for b in range(0, a):  # Replace the numbers with stars
        print("*", end=" ")
    print("")  # New line after each row
for c in range(4, 0, -1):  # We need to decrease the number of stars from 6th row to 9th so start with 4 and 0 -1 as
    # difference
    for d in range(0, c):
        print("*", end=" ")
    print("")

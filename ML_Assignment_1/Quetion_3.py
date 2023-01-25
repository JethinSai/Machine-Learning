sisters = ("Arya", "Aishwarya")  # In tuple values are unchangeable
brothers = ("Jethin", "Bharat", "Chaitan")
siblings = sisters + brothers  # Here we Join brothers and sisters tuples and assign it to siblings
print(f"I have {len(siblings)} siblings.")
family_members = siblings + ("Ram", "Lakshmi")  # Modify the siblings tuple and add the name of your father and
# mother and assign it to family_members
print(f"My family members are {family_members}")

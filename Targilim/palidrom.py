# Create two lists
list1 = [10, 20, 30]
list2 = [40, 50, 60]

# Print original lists
print("Original list1:", list1)
print("Original list2:", list2)

# Swap references using simultaneous assignment
list1, list2 = list2, list1

# Print swapped lists
print("Swapped list1:", list1)
print("Swapped list2:", list2)

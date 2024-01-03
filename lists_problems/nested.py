# Generating a multiplication table using nested loops
for i in range(1, 11):  # Outer loop for rows
    for j in range(1, 11):  # Inner loop for columns
        print(i * j, end="\t")  # Print the product of i and j
    print()  # Move to the next line for the new row

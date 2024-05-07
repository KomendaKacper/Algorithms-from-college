matrix = [[8, 10, 6, 7, 11], [5, 6, 2, 3, 4], [4, 9, 8, 6, 5]]

combined_rows = []

for i in range(len(matrix) - 1):
    combined_row = [x + y for x, y in zip(matrix[i], matrix[i+1])]
    combined_rows.append(combined_row)

print(combined_rows)

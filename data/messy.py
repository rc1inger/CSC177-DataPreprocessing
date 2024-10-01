import pandas as pd
import random
import numpy as np

# Read dataset
df = pd.read_csv('uci_heart_disease.csv')

# Random parameters
rows, cols = df.shape
num_of_messy_rows = random.randint(1, max(1, rows // 10))  # Ensure at least 1 messy row
max_num_of_missing_values = random.randint(0, 11)
max_num_of_duplicate_rows = random.randint(0, 5)
random_values = [10, 9345, 123, 956, 23.0, 83, 0.369, 3.1415259, 1.2, 69]
random_cells = []
duplicated_rows = []

# Replace random rows with random numerical values
for _ in range(num_of_messy_rows):
    rand_row = random.randint(0, rows - 1)
    df.iloc[rand_row] = random.choices(random_values, k=cols)  # Using random.choices for clearer intent

# Introduce missing values
for _ in range(max_num_of_missing_values):
    rand_row = random.randint(0, rows - 1)
    rand_col = random.randint(0, cols - 1)
    if random.random() < 0.5:  # 50% chance of replacing with np.nan
        df.iloc[rand_row, rand_col] = np.nan
        random_cells.append((rand_row, rand_col))

# Duplicate random rows
for _ in range(max_num_of_duplicate_rows):
    if random.random() < 0.5:  # 50% chance to duplicate
        rand_row = random.randint(0, rows - 1)
        duplicate_row = df.iloc[rand_row].copy()  # Copy to avoid reference issues

        # Insert the duplicated row at a random position
        insert_at = random.randint(0, rows)  # Include the last index
        df = pd.concat([df.iloc[:insert_at], pd.DataFrame([duplicate_row]), df.iloc[insert_at:]]).reset_index(drop=True)
        duplicated_rows.append(insert_at)

# Save the modified DataFrame to a new CSV file
df.to_csv('heart_disease.csv', index=False)

# Output information
print(f"Replaced values in {num_of_messy_rows} random rows with random numerical data.")
print(f"Replaced the following cells with np.nan: {random_cells}")
print(f'Duplicate row indices: {duplicated_rows}')
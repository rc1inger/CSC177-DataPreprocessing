import pandas as pd
import random
import numpy as np

# Read dataset
df = pd.read_csv('uci_heart_disease.csv')
df = df.astype(object)

# Random parameters
rows, cols = df.shape
num_of_messy_rows = random.randint(1, max(1, rows // 10))  # Ensure at least 1 messy row
max_num_of_missing_values = random.randint(0, 11)
max_num_of_duplicate_rows = random.randint(0, 5)
random_values = [10, 100, 123, 9, 23.0, 83, 0.369, 3.14, 1.2, 69]
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

def swap_column_values(df, num_swaps=5):
    # Select random columns and rows to swap values
    for _ in range(num_swaps):
        col1, col2 = random.sample(list(df.columns), 2)
        row = random.randint(0, len(df) - 1)
        # Swap the values between the two columns in the same row
        df.at[row, col1], df.at[row, col2] = df.at[row, col2], df.at[row, col1]
    return df

# Swap values between columns randomly
num_swaps = random.randint(1, 10)
df = swap_column_values(df, num_swaps)


# Duplicate random rows
for _ in range(max_num_of_duplicate_rows):
    if random.random() < 0.5:  # 50% chance to duplicate
        rand_row = random.randint(0, rows - 1)
        duplicate_row = df.iloc[rand_row].copy() 

        # Insert the duplicated row at a random position
        insert_at = random.randint(0, rows)  
        df = pd.concat([df.iloc[:insert_at], pd.DataFrame([duplicate_row]), df.iloc[insert_at:]]).reset_index(drop=True)
        duplicated_rows.append(insert_at)

#Adding unusual inconsistencies which are easy to spot
def create_logical_inconsistencies(df, n_inconsistencies=5):
    inconsistent_cells = []  # Track modified cells
    for _ in range(n_inconsistencies):
        rand_row = random.randint(0, len(df) - 1)
        # Creating an inconsistency: Age is unusually high but cholesterol is low
        if 'age' in df.columns and 'chol' in df.columns:
            df.at[rand_row, 'age'] = random.randint(80, 100)  # Unusually high age
            df.at[rand_row, 'chol'] = random.randint(100, 150)  # Unusually low cholesterol
            inconsistent_cells.append((rand_row, 'age'))
            inconsistent_cells.append((rand_row, 'chol'))
    return df, inconsistent_cells
df, logical_inconsistencies = create_logical_inconsistencies(df, n_inconsistencies=10)

# Save the modified DataFrame to a new CSV file
df.to_csv('heart_disease.csv', index=False)

# Output information
print(f"Replaced values in {num_of_messy_rows} random rows with random numerical data.")
print(f"Replaced the following cells with np.nan: {random_cells}")
print(f'Duplicate row indices: {duplicated_rows}')

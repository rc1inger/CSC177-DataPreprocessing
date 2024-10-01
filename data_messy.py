import pandas as pd
import random as rand

# Read dataset
df = pd.read_csv('uci_heart_disease.csv')

rows, cols = df.shape

# Random number of rows to make random, between 1 and one-tenth the number of rows.
num_of_messy_rows = rand.randint(1, rows // 10)
random_values = [10, 9345, 123, 956, 23.0, 83, 0.369, 3.1415259, 1.2, 69]
random_cells = []
duplicated_rows = []

# Replace selected rows with a random numerical value and potentially duplicate rows
for _ in range(num_of_messy_rows):
    rand_row = rand.randint(0, rows - 1)
    rand_col = rand.randint(0, cols - 1)  # Random column for '?' replacement
    random_value = rand.choice(random_values)
    
    # Replace each cell in the row with a random value
    for col in range(cols):
        col_dtype = df.iloc[:, col].dtype
        
        # Cast and assign values based on the column data type
        if pd.api.types.is_numeric_dtype(col_dtype):
            # Only cast float if the column can handle floats, else cast to int
            if df.iloc[:, col].dtype == 'float64':
                df.iloc[rand_row, col] = float(random_value)
            else:
                df.iloc[rand_row, col] = int(random_value)
        else:
            df.iloc[rand_row, col] = random_value

    # Randomly decide to replace a cell with a '?'
    if rand.random() < 0.3:  # 30% chance of replacing with '?'
        df.iloc[rand_row, rand_col] = '?'
        random_cells.append((rand_row, rand_col))

    # Randomly decide to duplicate the current row
    if rand.random() < 0.5:  # 50% chance of duplicating the row
        duplicate_row = df.iloc[rand_row].copy()  # Copy the row to avoid reference issues
        
        # Insert the duplicated row back into the DataFrame at a random position
        insert_at = rand.randint(0, rows - 1)  # Random position to insert the duplicate
        duplicated_rows.append(insert_at)
        df = pd.concat([df.iloc[:insert_at], pd.DataFrame([duplicate_row]), df.iloc[insert_at:]]).reset_index(drop=True)

# Save the modified DataFrame to a new CSV file
df.to_csv('messy_uci_heart_disease.csv', index=False)

# Output information
print(f"Replaced values in {num_of_messy_rows} random rows with random numerical data.")
print(f"Replaced the following cells with '?':")
print(random_cells)
print(f'Duplicat row numbers:')
print(duplicated_rows)

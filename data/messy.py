import pandas as pd
import random as rand

# Read dataset
df = pd.read_csv('uci_heart_disease.csv')
df = df.astype(object)

rows, cols = df.shape

# Random number of rows to make random data, between 1 and one-tenth the number of rows.
num_of_messy_rows = rand.randint(1, rows // 10)
max_num_of_missing_values = rand.randint(0, 11)
max_num_of_duplicate_rows = rand.randrange(0, 6)
random_values = [10, 9345, 123, 956, 23.0, 83, 0.369, 3.1415259, 1.2, 69]
random_value = rand.choice(random_values)
random_cells = []
duplicated_rows = []

# Replace number of messy rows with a random numerical value
for _ in range(num_of_messy_rows):
    rand_row = rand.randint(0, rows - 1)
    # Replace each cell in the row with a random value
    for col in range(cols):
        df.iloc[rand_row, col] = rand.choice(random_values)

for _ in range(max_num_of_missing_values):
    # Randomly decide to replace a cell with a '?'
    if rand.random() < 0.5:  # 50% chance of replacing with '?'
        rand_row = rand.randint(0, rows - 1)
        rand_col = rand.randint(0, cols - 1)
        df.iloc[rand_row, rand_col] = '?'
        random_cells.append((rand_row, rand_col))

for _ in range(max_num_of_duplicate_rows):
    # Randomly decide to duplicate the current row
    if rand.random() < 0.5:  # 50% chance
        rand_row = rand.randint(0, rows - 1)
        duplicate_row = df.iloc[rand_row].copy()  # Copy the row to avoid reference issues
        
        # Insert the duplicated row back into the DataFrame at a random position
        insert_at = rand.randint(0, rows - 1)  # Random position to insert the duplicate
        duplicated_rows.append(insert_at)
        df = pd.concat([df.iloc[:insert_at], pd.DataFrame([duplicate_row]), df.iloc[insert_at:]]).reset_index(drop=True)

# Save the modified DataFrame to a new CSV file
df.to_csv('heart_disease.csv', index=False)

# Output information
print(f"Replaced values in {num_of_messy_rows} random rows with random numerical data.")
print(f"Replaced the following cells with '?':")
print(random_cells)
print(f'Duplicate row numbers:')
print(duplicated_rows)

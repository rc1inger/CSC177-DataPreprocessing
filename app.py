import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Load the dataset and rename columns for clarity
data = pd.read_csv('data/heart_disease.csv')
data.columns = ['age', 'sex', 'cp', 'trestbps',
                'chol', 'fbs', 'restecg', 'thalach',
                'exang', 'oldpeak', 'slope', 'ca',
                'thal', 'disease']
# Drop the 'disease' column as it's the target variable for prediction
data = data.drop(['disease'], axis=1)

# Print the shape of the dataset to understand its dimensions
print(f'Number of instances = {data.shape[0]}')  # Number of rows
print(f'Number of attributes = {data.shape[1]}')  # Number of columns
print(data.head())  # Display the first few rows for a quick overview

# **Modularization: Created a function for duplicate removal**
def remove_duplicates(df):
    # Check for duplicate rows
    dups = df.duplicated()
    print(f'Number of duplicate rows = {dups.sum()}\n')  # Count duplicates
    # Drop duplicate rows from the DataFrame
    df_cleaned = df.drop_duplicates()
    print(f'Number of instances after dropping duplicates = {df_cleaned.shape[0]}')  # New row count
    return df_cleaned  # Return cleaned DataFrame

# Call the function to remove duplicates from the dataset
data2 = remove_duplicates(data)

# Replace '?' with NaN to handle missing values properly
data3 = data2.replace('?', np.nan)

# **Created a function to handle missing values**
def handle_missing_values(df):
    # Convert each column to numeric, coercing errors to NaN
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Print the count of missing values for each column
    print('Number of missing values:')
    for col in df.columns:
        print(f'\t{col}: {df[col].isna().sum()}')  # Count missing values
    
    # Replace missing values with the median of each column
    print('Replace missing values with median')
    for col in df.columns:
        df[col].fillna(df[col].median(), inplace=True)  # Use median to fill NaNs

    # Recount and print the number of missing values after imputation
    print('Number of missing values:')
    for col in df.columns:
        print(f'\t{col}: {df[col].isna().sum()}')  # Verify there are no missing values
    
    return df  # Return DataFrame with handled missing values

# Call the function to handle missing values in the dataset
data3 = handle_missing_values(data3)

# **Created a function to visualize missing values**
def visualize_missing_values(df):
    # Calculate missing values count
    missing_values = df.isna().sum()
    # Filter columns that have missing values
    missing_values = missing_values[missing_values > 0]
    
    # If there are missing values, plot them; otherwise, print a message
    if not missing_values.empty:
        missing_values.plot(kind='bar', figsize=(10, 5))  # Plot only columns with missing values
        plt.title('Missing Values Count')  # Title for the plot
        plt.xlabel('Features')  # X-axis label
        plt.ylabel('Count')  # Y-axis label
        plt.show()  # Display the plot
    else:
        print("No missing values to visualize.")  # Message for no missing values

# **Visualizing potential outliers using boxplots**
data3.boxplot(figsize=(20, 3))  # Initial boxplot for visual inspection
plt.title('Boxplot of Features Before Outlier Removal')  # Title for clarity
plt.show()  # Display the boxplot

# **Created a function for outlier removal**
def remove_outliers(df):
    # Standardize the DataFrame to identify outliers
    Z = (df - df.mean()) / df.std()  # Z-score normalization
    print(f'Number of rows before removing outliers = {Z.shape[0]}')  # Initial row count
    # Filter out rows with Z-scores outside the range [-3, 3]
    Z2 = df.loc[((Z > -3).sum(axis=1) == len(df.columns)) & ((Z <= 3).sum(axis=1) == len(df.columns)), :]
    print(f'Number of rows after removing outliers = {Z2.shape[0]}')  # Count after outlier removal
    return Z2  # Return DataFrame without outliers

# Call the function to remove outliers from the dataset
data3 = remove_outliers(data3)

# **Created a function to visualize cleaned data**
def visualize_data(df):
    # Boxplot of the cleaned DataFrame to visualize the distribution of features
    df.boxplot(figsize=(20, 3))  # Size of the plot
    plt.title('Boxplot of Features After Cleaning')  # Title for clarity
    plt.show()  # Display the plot

# Call the function to visualize the cleaned data
visualize_data(data3)

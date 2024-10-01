import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

data = pd.read_csv('data/heart_disease.csv')
data.columns = ['age', 'sex', 'cp', 'trestbps',
                'chol', 'fbs', 'restecg', 'thalach',
                'exang', 'oldpeak', 'slope', 'ca',
                'thal', 'disease']
data = data.drop(['disease'],axis=1)

# Shape of the dataset
print(f'Number of instances = {data.shape[0]}')
print(f'Number of attributes = {data.shape[1]}')
print(data)

# Duplicate Data
dups = data.duplicated()
print(f'Number of duplicate rows = {dups.sum()}\n')
print('Removing duplicate rows\n')
data2 = data.drop_duplicates()
print(f'Number of instances after dropping duplicates = {data2.shape[0]}')
print(data2)

# Missing Values replace with NaN
data3 = data2.replace('?', np.nan)

# Convert columns to numeric, coercing errors
for col in data3.columns:
    data3[col] = pd.to_numeric(data3[col], errors='coerce')
    
print(data3)

print('Number of missing values:')
for col in data3.columns:
    print(f'\t{col}: {data3[col].isna().sum()}')

# Missing Values replace with Median value of attribute
print('Replace missing values with median')
for col in data3.columns:
    column = f'{col}'
    datacol = data3[column]
    data3[column] = datacol.fillna(datacol.median())

# Missing Values recount and print dataset
print('Number of missing values:')
for col in data3.columns:
    print(f'\t{col}: {data3[col].isna().sum()}')
print(data3)

# Outliers
for col in data3.columns:
    column = f'{col}'
    datacol = data3[column]
    data3[col] = pd.to_numeric(data3[column])

data3.boxplot(figsize=(20,3))
plt.show()

Z = (data3-data3.mean())/data3.std()
print(f'Number of rows before removing outliers = {Z.shape[0]}')
Z2 = Z.loc[((Z > -3).sum(axis=1)==13) & ((Z <= 3).sum(axis=1)==13),:]
print(f'Number of rows after removing outliers = {Z2.shape[0]}')
print(Z2)
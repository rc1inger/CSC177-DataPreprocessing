import pandas as pd
import numpy as np

data = pd.read_csv('data/heart_disease.csv')

# Data Quality Issues
data.columns = ['age', 'sex', 'cp', 'trestbps',
                'chol', 'fbs', 'restecg', 'thalach',
                'exang', 'oldpeak', 'slope', 'ca',
                'thal', 'disease']


data = data.drop(['disease'],axis=1)

# using f string to format since Python 3.6
print(f'Number of instances = {data.shape[0]}')
print(f'Number of attributes = {data.shape[1]}')

# Missing Values
# Replace blank cells with NaN
data= data.replace('?', np.nan)

print('Number of missing values:')
for col in data.columns:
    print(f'\t{col}: {data[col].isna().sum()}')


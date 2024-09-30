import pandas as pd
#github won't host large files
data = pd.read_csv('steam_app_data.csv')


''' remove attributes
type - because the data will be all games and this column has info that was scaped such as Terms of Use and Copyright info

'''

# using f string to format since Python 3.6
print(f'Number of instances = {data.shape[0]}')
print(f'Number of attributes = {data.shape[1]}')

#data.head()


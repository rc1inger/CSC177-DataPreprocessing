import pandas as pd
import numpy as np

data = pd.read_csv('steam_app_data.csv')

# Data Quality Issues
data.columns = ['type', 'name', 'steam_appid', 'required_age',
                'is_free', 'controller_support', 'dlc',
                'detailed_description', 'about_the_game',
                'short_description', 'fullgame',
                'supported_languages', 'header_image', 'website',
                'pc_requirements', 'mac_requirements',
                'linux_requirements', 'legal_notice', 'drm_notice',
                'ext_user_account_notice', 'developers',
                'publishers', 'demos', 'price_overview',
                'packages', 'package_groups', 'platforms',
                'metacritic', 'reviews', 'categories', 'genres',
                'screenshots', 'movies', 'recommendations',
                'achievements', 'release_date', 'support_info',
                'background', 'content_descriptors'
]

''' remove attributes
type - because the attribute should always be "games" and this column has dirty info that was scraped.
controller_support - incomplete data. It only shows full, but doesn't say anything like joystick or anything useful
dlc - unsure what this info is because it shows a string of numbers. Maybe a steam_appid?
detailed_description - not needed for analytics
about_the_game - not needed for analytics
short_description - not needed for analytics
fullgame - attribute added by mistake
header_image - not needed for analytics
website - not needed for analytics
pc_requirements - ### CAN THIS BE CLEANED UP? ###
mac_requirements - ^^^
linux_requirements - ^^^
legal_notice - not needed for analytics
drm_notice - not needed for analytics
ext_user_account_notice - not needed for analytics
demos - not needed for analytics
packages - not needed for analytics
package_groups - not needed for analytics
metacritic - not needed for analytics
reviews - not needed for analytics
screenshots - not needed for analytics
movies - not needed for analytics
recommendations - not needed for analytics
achievements - not needed for analytics
support_info - not needed for analytics
background - not needed for analytics
content_descriptors - not needed for analytics
'''
data = data.drop(['type', 'controller_support', 'dlc',
             'detailed_description', 'about_the_game',
             'short_description', 'fullgame',
             'header_image', 'website', 'pc_requirements',
             'mac_requirements', 'linux_requirements',
             'legal_notice', 'drm_notice',
             'ext_user_account_notice', 'demos', 'packages',
             'package_groups', 'metacritic', 'reviews',
             'screenshots', 'movies', 'recommendations',
             'achievements', 'support_info', 'background',
             'content_descriptors'
],axis=1)

# using f string to format since Python 3.6
print(f'Number of instances = {data.shape[0]}')
print(f'Number of attributes = {data.shape[1]}')

''' We are keeping these attributes
name
steam_appid
required_age
is_free
supported_laguages - make it a 1 if is in English
developer
publisher
price_overview - too hard to clean?
platforms
categories
genres
release_date
'''

# Missing Values
# Replace blank cells with NaN
data= data.replace(r'^\s*$', np.nan, regex=True)

print('Number of missing values:')
for col in data.columns:
    print(f'\t{col}: {data[col].isna().sum()}')


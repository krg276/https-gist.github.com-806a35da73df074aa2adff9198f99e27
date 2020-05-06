import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

# View csv file

#print(ad_clicks.head())

# Which add playform is getting the most views, i.e how many user ids

mostviews = ad_clicks.groupby('utm_source').user_id.count().reset_index()

# Creates a new column where ad_click_timestamp isnull

ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()

# Percentage of people who clicked on adds form each source

clicks_by_source = ad_clicks\
   .groupby(['utm_source',
             'is_click'])\
   .user_id.count()\
   .reset_index()

#Pivot the above

clicks_pivot = clicks_by_source\
   .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
   .reset_index()

# New column for percent clicked from utm source

clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True] + clicks_pivot[False])







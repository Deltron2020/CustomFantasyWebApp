from basketball_reference_web_scraper import client
import pandas as pd


stats = client.players_season_totals(season_end_year=2024)

df = pd.DataFrame.from_dict(stats)

print(df.columns)
def label_position(row):
   if row['positions1'] == [{'Position.CENTER':'CENTER'}]:
      return 'C'
   if row['positions1'] == ['Position.POWER_FORWARD']:
      return 'PF'
   if row['positions1'] == ['Position.SHOOTING_GUARD']:
      return 'SG'
   if row['positions1'] == ['SMALL_FORWARD']:
      return 'SF'
   if row['positions1'] == ['<Position.CENTER: ''CENTER''>']:
      return 'PG'
   return 'Other'

df['positions1'] = df['positions'].astype('string')

df['positions1']  = df['positions1'].str.replace('CENTER','C')

print(df['positions1'].head(15))


print(df.head(5))
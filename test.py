from basketball_reference_web_scraper import client
import pandas as pd


stats = client.players_season_totals(season_end_year=2024)
df = pd.DataFrame.from_dict(stats)

print(df.columns)

def label_position(row):
   if 'CENTER' in row['positions']:
      return 'C'
   if 'POWER_FORWARD' in row['positions']:
      return 'PF'
   if 'SHOOTING_GUARD' in row['positions']:
      return 'SG'
   if 'SMALL_FORWARD' in row['positions']:
      return 'SF'
   if 'POINT GUARD' in row['positions']:
      return 'PG'
   return 'Other'

# changing to strings
df['positions'] = df['positions'].astype('string')
df['team'] = df['team'].astype('string')

# adding new columns
df['team'] = df['team'].str.replace('_', ' ').str.replace('Team.', '')
df['position'] = df.apply(label_position, axis=1)
df['id'] = df.index + 1


max_id = (
   df
      .filter(['id','name'])#,'age', 'team', 'position', 'points'])
      #.query("(name == 'P.J. Washington')")
      #.drop_duplicates()
      .groupby(['name'], as_index=False)
      ['id'].max()
      #['points'].sum()
      #.sort_values(by='position', ascending=False)
)

current_team = (
   df
      .filter(['id','team'])
)

player_stats = (
   df
      .filter(['name', 'games_played', 'minutes_played', 'offensive_rebounds', 'defensive_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'personal_fouls', 'points'])
      .groupby(['name'], as_index=False)
      .agg(
      {
         'games_played': 'sum',
         'minutes_played': 'sum',
         'offensive_rebounds': 'sum',
         'defensive_rebounds': 'sum',
         'assists': 'sum',
         'steals': 'sum',
         'blocks': 'sum',
         'turnovers': 'sum',
         'personal_fouls': 'sum',
         'points': 'sum'
      }
   )
)


#print(max_id.merge(current_team, on='id', how='inner').merge(player_stats, on='name', how='inner'))
def players_df():
   max_id = (
      df
      .filter(['id', 'name', 'age'])  # ,'age', 'team', 'position', 'points'])
      # .query("(name == 'P.J. Washington')")
      # .drop_duplicates()
      .groupby(['name','age'], as_index=False)
      ['id'].max()
      # ['points'].sum()
      # .sort_values(by='position', ascending=False)
   )

   current_team = (
      df
      .filter(['id', 'team', 'position'])
   )

   player_max_id = max_id.merge(current_team, on='id', how='inner')

   return player_max_id

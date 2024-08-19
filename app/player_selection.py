from app.player_totals_dataframe import get_player_totals_dataframe
df = get_player_totals_dataframe(2024)

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


def players_df():
   max_id = (
      df
      .filter(['id', 'name', 'age'])  # ,'age', 'team', 'position', 'points'])
      # .query("(name == 'P.J. Washington')")
      # .drop_duplicates()
      .groupby(['name','age'], as_index=False)
      ['id'].max()
      # .sort_values(by='position', ascending=False)
   )

   current_team = (
      df
      .filter(['id', 'team', 'position'])
   )

   player_max_id = max_id.merge(current_team, on='id', how='inner')

   return player_max_id

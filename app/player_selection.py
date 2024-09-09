from app.player_totals_dataframe import get_player_totals_dataframe
#df = get_player_totals_dataframe(2024)
dict = get_player_totals_dataframe(2024)

df = dict[2024]
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
df['rebounds'] = df['offensive_rebounds'] + df['defensive_rebounds']
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


def player_stat_search(player_name):
   player_stats = (
      df
      .filter(['name', 'age', 'points', 'assists', 'rebounds', 'blocks', 'steals', 'turnovers', 'games_played'])
      .query(f"(name == '{player_name}')")
      # .drop_duplicates()
      .groupby(['name', 'age'], as_index=False)
      [['points','assists','rebounds','blocks','steals','turnovers','games_played']].sum().sum()
      # .sort_values(by='position', ascending=False)
   )

   total_stats = player_stats.to_dict()
   ppg = round(total_stats['points'] / total_stats['games_played'], 2)
   apg = round(total_stats['assists'] / total_stats['games_played'], 2)
   rpg = round(total_stats['rebounds'] / total_stats['games_played'], 2)
   bpg = round(total_stats['blocks'] / total_stats['games_played'], 2)
   spg = round(total_stats['steals'] / total_stats['games_played'], 2)
   tpg = round(total_stats['turnovers'] / total_stats['games_played'], 2)
   total_stats['points_per_game'] = ppg
   total_stats['assists_per_game'] = apg
   total_stats['rebounds_per_game'] = rpg
   total_stats['blocks_per_game'] = bpg
   total_stats['steals_per_game'] = spg
   total_stats['turnovers_per_game'] = tpg

   #print(total_stats)

   return total_stats

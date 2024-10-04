from app.player_totals_dataframe import get_player_totals_dataframe
year = int(2024)

dict = get_player_totals_dataframe(year)
df = dict[year]
#py_df = dict[year-1]



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


def update_dataframe(dataframe):
   # changing to strings
   dataframe['positions'] = dataframe['positions'].astype('string')
   dataframe['team'] = dataframe['team'].astype('string')

   # adding new columns
   dataframe['rebounds'] = dataframe['offensive_rebounds'] + dataframe['defensive_rebounds']
   dataframe['team'] = dataframe['team'].str.replace('_', ' ').str.replace('Team.', '')
   dataframe['position'] = dataframe.apply(label_position, axis=1)
   dataframe['id'] = dataframe.index + 1


update_dataframe(df)
#update_dataframe(py_df)

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


def py_player_stat_search(player_name):
   py_player_stats = (
      py_df
      .filter(['name', 'age', 'points', 'assists', 'rebounds', 'blocks', 'steals', 'turnovers', 'games_played'])
      .query(f"(name == '{player_name}')")
      .groupby(['name', 'age'], as_index=False)
      [['points','assists','rebounds','blocks','steals','turnovers','games_played']].sum().sum()
   )

   py_total_stats = py_player_stats.to_dict()
   py_ppg = round(py_total_stats['points'] / py_total_stats['games_played'], 2)
   py_apg = round(py_total_stats['assists'] / py_total_stats['games_played'], 2)
   py_rpg = round(py_total_stats['rebounds'] / py_total_stats['games_played'], 2)
   py_bpg = round(py_total_stats['blocks'] / py_total_stats['games_played'], 2)
   py_spg = round(py_total_stats['steals'] / py_total_stats['games_played'], 2)
   py_tpg = round(py_total_stats['turnovers'] / py_total_stats['games_played'], 2)
   py_total_stats['points_per_game'] = py_ppg
   py_total_stats['assists_per_game'] = py_apg
   py_total_stats['rebounds_per_game'] = py_rpg
   py_total_stats['blocks_per_game'] = py_bpg
   py_total_stats['steals_per_game'] = py_spg
   py_total_stats['turnovers_per_game'] = py_tpg

   #print(py_total_stats)

   return py_total_stats
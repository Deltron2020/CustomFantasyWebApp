from app.player_totals_dataframe import get_player_totals_dataframe
dict = get_player_totals_dataframe(2024)

df = dict[2024]

def points_leaders():
   top5points = (df
                  .filter(['name', 'points'])
                  #.query("(name == 'P.J. Washington')")
                  .groupby(['name'], as_index=False)
                     ['points'].sum()
                     .sort_values(by='points', ascending=False)
                    .head(5)
   ).to_dict()

   return top5points


def blocks_leaders():
   top5blocks = (df
                 .filter(['name', 'blocks'])
                 .groupby(['name'], as_index=False)
                 ['blocks'].sum()
                 .sort_values(by='blocks', ascending=False)
                 .head(5)
   ).to_dict()

   return top5blocks


def assists_leaders():
   top5assists = (df
                  .filter(['name', 'assists'])
                  .groupby(['name'], as_index=False)
                  ['assists'].sum()
                  .sort_values(by='assists', ascending=False)
                  .head(5)
   ).to_dict()

   return top5assists


def steals_leaders():
   top5steals = (df
                  .filter(['name', 'steals'])
                  .groupby(['name'], as_index=False)
                  ['steals'].sum()
                  .sort_values(by='steals', ascending=False)
                  .head(5)
   ).to_dict()

   return top5steals


def o_rebounds_leaders():
    top5offensive_rebounds = (df
                  .filter(['name', 'offensive_rebounds'])
                  .groupby(['name'], as_index=False)
                  ['offensive_rebounds'].sum()
                  .sort_values(by='offensive_rebounds', ascending=False)
                  .head(5)
    ).to_dict()

    return top5offensive_rebounds


def d_rebounds_leaders():
    top5defensive_rebounds = (df
                  .filter(['name', 'defensive_rebounds'])
                  .groupby(['name'], as_index=False)
                  ['defensive_rebounds'].sum()
                  .sort_values(by='defensive_rebounds', ascending=False)
                  .head(5)
    ).to_dict()

    return top5defensive_rebounds


def turnover_leaders():
    top5turnovers = (df
                  .filter(['name', 'turnovers'])
                  .groupby(['name'], as_index=False)
                  ['turnovers'].sum()
                  .sort_values(by='turnovers', ascending=False)
                  .head(5)
    ).to_dict()

    return top5turnovers


def fouls_leaders():
    top5fouls = (df
                  .filter(['name', 'personal_fouls'])
                  .groupby(['name'], as_index=False)
                  ['personal_fouls'].sum()
                  .sort_values(by='personal_fouls', ascending=False)
                  .head(5)
    ).to_dict()

    return top5fouls

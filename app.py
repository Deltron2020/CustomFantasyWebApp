from basketball_reference_web_scraper import client
import pandas as pd

#stats = client.players_advanced_season_totals(season_end_year=2024)
stats = client.players_season_totals(season_end_year=2024)

df = pd.DataFrame.from_dict(stats)

print(df.columns)
print('testing!')
print(df
        .filter(['name','points'])
      .query("name.str.find('Kevin')>=0")
      .head(10)
      )

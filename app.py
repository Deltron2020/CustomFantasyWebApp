from basketball_reference_web_scraper import client
import pandas as pd
from flask import render_template, request
from app import create_app

app = create_app()

#stats = client.players_advanced_season_totals(season_end_year=2024)
try:
    stats = client.players_season_totals(season_end_year=2024)
except:
    stats = {}
    print('connection to stats failed')



df = pd.DataFrame.from_dict(stats)

#df.insert(2,"name_lower", df['name'].str.lower(), True)
#print(df.columns)

#df.to_csv('C:/Users/tyler/Projects/CustomFantasyWebApp/players.csv', index=False)


@app.route("/")
def web_app_home():
    players = (df
               .filter(['name', 'positions', 'age', 'team'])
               ).to_dict()

    top5points = (df
               .filter(['name', 'points'])
               .sort_values(['points'], ascending=False)
               .head(5)
               ).to_dict()

    pointsNamesList = list(top5points['name'].values())
    pointsPointsList = list(top5points['points'].values())

    top5blocks = (df
               .filter(['name', 'blocks'])
               .sort_values(['blocks'], ascending=False)
               .head(5)
               ).to_dict()

    blocksNamesList = list(top5blocks['name'].values())
    blocksBlocksList = list(top5blocks['blocks'].values())

    #print(players)

    return render_template('FA_Home.html',
                           dataframe=players,
                           top5points=pointsPointsList, top5points_names=pointsNamesList,
                           top5blocks=blocksBlocksList, top5blocks_names=blocksNamesList)


print(__name__)
# only if we run this file, not if we import it are we going to execute this line (start the app)
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

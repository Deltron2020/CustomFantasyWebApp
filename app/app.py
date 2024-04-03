from basketball_reference_web_scraper import client
import pandas as pd
from flask import Flask, render_template, request

#stats = client.players_advanced_season_totals(season_end_year=2024)
stats = client.players_season_totals(season_end_year=2024)

df = pd.DataFrame.from_dict(stats)
df.insert(2,"name_lower", df['name'].str.lower(), True)
#print(df.columns)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def web_app_home():
    data = request.args
    player = {'PlayerSearch': ''}
    for i in data:
        if (len(data[i])) > 0:
            value = {i: data[i]}
            player.update(value)
            break

    players = (df
               .filter(['name', 'name_lower', 'points', 'positions', 'age', 'team'])
               .query(f"name_lower.str.find('{player['PlayerSearch'].lower()}')>=0")
               #.head(10)
               ).to_dict()

    return render_template('FA_Home.html', dataframe=players)


print(__name__)
if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
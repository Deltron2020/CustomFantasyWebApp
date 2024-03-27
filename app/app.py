from basketball_reference_web_scraper import client
import pandas as pd
from flask import Flask, render_template, request

#stats = client.players_advanced_season_totals(season_end_year=2024)
stats = client.players_season_totals(season_end_year=2024)

df = pd.DataFrame.from_dict(stats)
#print(df.columns)

players = (df
            .filter(['name','points'])
            .query("name.str.find('Smith')>=0")
            .head(10)
            ).to_dict()


app = Flask(__name__)

@app.route("/")
def web_app_home():
    return render_template('FA_Home.html', dataframe=players)


print(__name__)
if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
from basketball_reference_web_scraper import client
import pandas as pd


def get_player_totals_dataframe(year: int):
    try:
        #advstats = client.players_advanced_season_totals(season_end_year=year)
        stats = client.players_season_totals(season_end_year=year)
        df = pd.DataFrame.from_dict(stats)
    except Exception as e:
        print(e)
        df = pd.DataFrame()

    return df
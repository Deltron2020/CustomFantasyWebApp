from basketball_reference_web_scraper import client
import pandas as pd

def get_player_totals_dataframe(year: int):
    try:
        #advstats = client.players_advanced_season_totals(season_end_year=year)
        stats = client.players_season_totals(season_end_year=year)
        prior_stats = client.players_season_totals(season_end_year=year-1)

        df = pd.DataFrame.from_dict(stats)
        py_df = pd.DataFrame.from_dict(prior_stats)

        stat_dict = {year: df, year-1: py_df}

    except Exception as e:
        print(e)
        df = pd.DataFrame()
        stat_dict = {}

    return stat_dict #df

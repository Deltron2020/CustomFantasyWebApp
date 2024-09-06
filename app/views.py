from flask import render_template, Blueprint, request
from app.player_selection import players_df, player_stat_search
from app.season_leaders import (points_leaders, blocks_leaders, assists_leaders, steals_leaders, o_rebounds_leaders, d_rebounds_leaders, turnover_leaders, fouls_leaders)


views = Blueprint('views',__name__)


@views.route("/")
def home():
    player_search_df = players_df().to_dict()
    return render_template('FA_Home.html',player_search_table=player_search_df)



@views.route("/stat_leaders")
def web_app_home():

    top5points = points_leaders()
    pointsNamesList = list(top5points['name'].values())
    pointsPointsList = list(top5points['points'].values())

    top5blocks = blocks_leaders()
    blocksNamesList = list(top5blocks['name'].values())
    blocksBlocksList = list(top5blocks['blocks'].values())

    top5assists = assists_leaders()
    assistsNamesList = list(top5assists['name'].values())
    assistsAssistsList = list(top5assists['assists'].values())

    top5steals = steals_leaders()
    stealsNamesList = list(top5steals['name'].values())
    stealsStealsList = list(top5steals['steals'].values())

    top5o_rebounds = o_rebounds_leaders()
    oReboundsNamesList = list(top5o_rebounds['name'].values())
    reboundsOffReboundsList = list(top5o_rebounds['offensive_rebounds'].values())

    top5d_rebounds = d_rebounds_leaders()
    dReboundsNamesList = list(top5d_rebounds['name'].values())
    reboundsDefReboundsList = list(top5d_rebounds['defensive_rebounds'].values())

    top5turnover = turnover_leaders()
    turnoverNamesList = list(top5turnover['name'].values())
    turnoverTurnoverList = list(top5turnover['turnovers'].values())

    top5fouls = fouls_leaders()
    foulsNamesList = list(top5fouls['name'].values())
    foulsFoulsList = list(top5fouls['personal_fouls'].values())


    return render_template('FA_HomeCharts.html',
                           top5points=pointsPointsList, top5points_names=pointsNamesList,
                           top5blocks=blocksBlocksList, top5blocks_names=blocksNamesList,
                           top5assists=assistsAssistsList, top5assists_names=assistsNamesList,
                           top5steals=stealsStealsList, top5steals_names=stealsNamesList,
                           top5o_rebounds=reboundsOffReboundsList, top5o_rebounds_names=oReboundsNamesList,
                           top5d_rebounds=reboundsDefReboundsList, top5d_rebounds_names=dReboundsNamesList,
                           top5turnovers=turnoverTurnoverList, top5turnovers_names=turnoverNamesList,
                           top5fouls=foulsFoulsList, top5fouls_names=foulsNamesList)


@views.route("/player/<name>")
def web_app_player(name):
    return render_template('FA_Player.html', name=name, stats=player_stat_search(name))

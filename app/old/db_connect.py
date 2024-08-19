from sqlalchemy import create_engine
import urllib
from app import create_app, app
import psycopg2



conn = urllib.parse.quote_plus(
    'Data Source Name=WebAppDataSource;'  # name of odbc connection created on server
    'Driver={ODBC Driver 17 for SQL Server};'
    f"Server={app.config['DB_SERVER_NAME']};"
    f"Database={app.config['DATABASE']};"
    'Trusted_connection=yes;'
    f"Username={app.config['USERNAME']};"
    f"Password={app.config['PASSWORD']};"
)


try:

    #coxn = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn))
    #coxn = create_engine('postgresql+psycopg2://root:9eDBhkVxCjDfZ3rVvijD3PjSgAKcq9nu@dpg-cohlu9djm4es739b5pf0-a.ohio-postgres.render.com/app_db_l1rs')
    coxn = create_engine('postgresql+psycopg2:///?odbc_connect={}'.format(conn))
    print("Passed")

except:
    print("Failed!")
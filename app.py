from basketball_reference_web_scraper import client
import pandas as pd
from flask import render_template, request
from app import create_app

app = create_app()


print(__name__)
# only if we run this file, not if we import it are we going to execute this line (start the app)
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

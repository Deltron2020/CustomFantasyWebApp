from sqlalchemy import text
from app.old.db_connect import coxn

def insert_user_sql(username, email, password, dob, promo):
    with coxn.connect() as connection:
        sql = text(f"""
                    INSERT INTO users 
                        (username, 
                        email, 
                        password, 
                        dob, 
                        promo,
                        createdate) 
                    VALUES 
                        (:username,
                        :email,
                        :password,
                        :dob,
                        :promo,
                        NOW())
                    """)

        connection.execute(sql, username=username, email=email, password=password, dob=dob, promo=promo)
        connection.commit()

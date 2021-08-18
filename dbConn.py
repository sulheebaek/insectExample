import pymysql
import pandas as pd

def dfFromDB(query):
    """
    @parameters query: str type, sql query string
    @return sql_df: pandas DataFrame
    """
    certInfo = open('./certificate.inf')
    username = certInfo.readline().strip()
    passwd = certInfo.readline().strip()
    certInfo.close()


    db = pymysql.connect(host='202.31.147.129',
                    user=username,
                    password=passwd,
                    database='insect',
                    port=13307)
    cursor = db.cursor()
    cursor.execute(query)
    sql_df = pd.DataFrame(cursor.fetchall())
    sql_df.columns = list(zip(*cursor.description))[0]
    db.close()

    return sql_df





#install sqlalchemy 
#install MySQLdb
'''paina rendu insatll chey pip install tho
    ee method avtundhi naa system lo MySQLdb install avvadam ledhu
    create_engine dhaggra error vasttundhi naku nuv try install chesi ee code ni
'''
import mysql.connector as c
import pymysql as p
import pandas as pd
from sqlalchemy import Float, create_engine
import sqlalchemy
p.install_as_MySQLdb()
engine = create_engine('mysql://root:honeychandu@localhost/project')# ee string dhaggara na username = root,password = honeychandu,database = project so nee names batti replace chesko ra 
print(engine)
df = pd.read_excel("/Users/mr.chandu/Desktop/Project/flask_mongo/excel_L.xls")
f1 = pd.DataFrame(df)
f1.to_sql("sqlb",con= engine,if_exists="append",index='False')
#,dtype={"SSC Percentage": sqlalchemy.types.Float(precision=3,asdecimal=True)}
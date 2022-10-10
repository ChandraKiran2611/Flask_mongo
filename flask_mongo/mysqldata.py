import mysql.connector as c
import xlrd
con = c.connect(host = "localhost",user = "root",password = "honeychandu",database = 'project')
cursor = con.cursor()
l =[]
x= []
file ="/Users/mr.chandu/Desktop/Project/flask_mongo/excel_L.xls"
a = xlrd.open_workbook(file)
sheet = a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,21):
    x = list(sheet.row_values(i))
    #s = float(x[3])
   # l.append(x)
print(float(x[3]))
'''query = "insert into nsritData(Roll,caste,ssc_percentage,inter_percentage)values(%s,%s,%f,%s)"
cursor.executemany(query,l)
con.commit()
con.close()''' 
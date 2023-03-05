import os
import sqlite3
import pandas as pd

cwd = os.getcwd()
#data_url = cwd+'/static/csv/addresses.xlsx'
data_url = cwd+'/static/csv/skillsStatus.xlsx'
#headers = ['first_name','last_name','address','city','state','zip']
headers = ['id','name','title','company','availability','experience','baselineClearance','expertisedAreas','toolsAndTechnologies']

#data_table = pd.read_csv(data_url, header=None, names=headers, converters={'zip': str})
data_table = pd.read_excel(data_url, header=0, names=headers, converters={'zip': str})
#print(data_table)

if os.path.exists('dstig001.db'):
    os.remove('dstig001.db')

conn = sqlite3.connect('dstig001.db', check_same_thread=False)

"""
data_table.to_sql('data_table', conn, dtype={
    'first_name':'VARCHAR(256)',
    'last_name':'VARCHAR(256)',
    'address':'VARCHAR(256)',
    'city':'VARCHAR(256)',
	'state':'VARCHAR(2)',
	'zip':'VARCHAR(5)',
})

"""
data_table.to_sql('data_table001', conn, dtype={
    'id':'VARCHAR(20)',
    'name':'VARCHAR(20)',
    'title':'VARCHAR(20)',
    'company':'VARCHAR(10)',
	'availability':'VARCHAR(10)',
	'experience':'INT(2)',
    'baselineClearance':'VARCHAR(10)',
    'expertisedAreas':'VARCHAR(256)',
	'toolsAndTechnologies':'VARCHAR(256)',
})

conn.row_factory = sqlite3.Row

def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows

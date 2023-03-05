from flask import Flask, request, redirect, render_template
import sys

app = Flask(__name__)

@app.route('/') 
def sql_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM data_table001''')
    msg = 'SELECT * FROM data_table001'
    return render_template('sqldatabase.html', results=results, msg=msg)   

@app.route('/insert',methods = ['POST', 'GET']) 
def sql_datainsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        last_name = request.form['last_name']
        first_name = request.form['first_name']  
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        sql_edit_insert(''' INSERT INTO data_table (first_name,last_name,address,city,state,zip) VALUES (?,?,?,?,?,?) ''', (first_name,last_name,address,city,state,zip) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'INSERT INTO data_table (first_name,last_name,address,city,state,zip) VALUES ('+first_name+','+last_name+','+address+','+city+','+state+','+zip+')'
    return render_template('sqldatabase.html', results=results, msg=msg) 

@app.route('/delete',methods = ['POST', 'GET'])
def sql_datadelete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        lname = request.args.get('lname')
        fname = request.args.get('fname')
        sql_delete(''' DELETE FROM data_table where first_name = ? and last_name = ?''', (fname,lname) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'DELETE FROM data_table WHERE first_name = ' + fname + ' and last_name = ' + lname
    return render_template('sqldatabase.html', results=results, msg=msg)

@app.route('/query_edit',methods = ['POST', 'GET'])
def sql_editlink():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        id = request.args.get('id')
        name = request.args.get('name')
        eresults = sql_query2(''' SELECT * FROM data_table001 where id = ? and name = ?''', (id,name))
    results = sql_query(''' SELECT * FROM data_table001''')
    return render_template('sqldatabase.html', eresults=eresults, results=results)

@app.route('/edit',methods = ['POST', 'GET'])
def sql_dataedit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        old_id = request.form['old_id']
        old_name = request.form['old_name']
        id = request.form['id']
        name = request.form['name']
        title = request.form['title']
        company = request.form['company']
        availability = request.form['availability']
        experience = request.form['experience']
        baselineClearance = request.form['baselineClearance']
        expertisedAreas = request.form['expertisedAreas']
        toolsAndTechnologies = request.form['toolsAndTechnologies']
        sql_edit_insert(''' UPDATE data_table001 set id=?,name=?,title=?,company=?,availability=?,experience=?,baselineClearance=?,expertisedAreas=?,toolsAndTechnologies=? WHERE id=? and name=? ''', (id,name,title,company,availability,experience,baselineClearance,expertisedAreas,toolsAndTechnologies,old_id,old_name) )
    results = sql_query(''' SELECT * FROM data_table001''')
    #msg = 'UPDATE data_table set id = ' + id + ', name = ' + name + ', address = ' + address + ', city = ' + city + ', state = ' + state + ', zip = ' + zip + ' WHERE first_name = ' + old_id + ' and last_name = ' + old_name
    return render_template('sqldatabase.html', results=results, msg="")

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

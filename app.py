from flask import Flask, render_template, request,redirect,url_for
import mysql.connector

conn =mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'ems'
    )

mycursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('first.html')


@app.route('/add')
def add():
    return render_template('add.html')



@app.route('/edit')
def edit():
    
    
    return render_template('edit.html')

@app.route('/view')
def view():
    
    query=("select * from employees")
    mycursor.execute(query)
    result=mycursor.fetchall()
    return render_template('view.html', sqldata=result)

@app.route('/delete')
def delete():
    return render_template('delete.html')


@app.route('/read', methods =['POST'])
def read():
    id = request.form['empid']
    name = request.form['empname']
    salary = request.form['empsalary']
    dept = request.form['empdept']
    
    query = 'insert into employees values(%s, %s, %s, %s)'
    data =(id, name, salary, dept)
    mycursor.execute(query,data)
    conn.commit()
    
    return render_template('add.html') 

@app.route('/edit', methods =['POST', 'GET'])
def edit_emp():
    if request.method == 'POST':
        empid = request.form['empid']
        name = request.form['empname']
        salary = request.form['empsal']
        dept = request.form['empdept']
        

        query = "UPDATE employees SET emp_name=%s, emp_salary=%s, emp_dept=%s WHERE emp_id=%s"
        data = (name, salary, dept, empid)  
        mycursor.execute(query, data)
        conn.commit()
        return redirect(url_for('view'))

    return render_template('edit.html')


@app.route('/delete_emp', methods=['GET', 'POST']) 
def delete_emp():
    if request.method == 'POST':
        empid = request.form['employee_id']
        query = "DELETE FROM employees WHERE emp_id=%s"
        data = (empid,)  
        mycursor.execute(query, data)
        conn.commit()

        return redirect(url_for('view')) 

    return render_template('delete.html')

    


if __name__ =='__main__':
    app.run(debug=True)

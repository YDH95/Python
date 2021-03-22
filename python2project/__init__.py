from flask import Flask, render_template, request, session
import mysql
import mysql.connector
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "010"  # 고유 비밀키

def db_execute():
    dbconfig = {'host': 'localhost', 'user': 'root',
                'password': '', 'database': 'g_homepage'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    return conn, cursor

@ app.route('/')  # 담당경로
def g_home() -> "html":
    a = session.get("(u_id", None)
    return render_template("g_home.html", a=a)

@app.route("/login/", methods=['POST'])
def g_login():
    a = request.form['u_id']  # g_write에 name
    b = request.form['u_pw']
    conn, cur = db_execute()
    SQL = """SELECT * FROM user WHERE g_id = %s and g_pw = %s"""
    cur.execute(SQL, (a, b))
    alldata = cur.fetchall() 
    cur.close()
    conn.close()
    info = ''
    if(len(alldata) >= 1):
        if a == 'admin':
            return redirect('/admin/')
        print("logged in...")
        session.clear()
        session["u_id"] = a
        session["u_iw"] = b
        return redirect('/')
    else:
        print("who are you...")
    return render_template("g_login.html", info='다시입력해주세요.')

@app.route('/admin/')
def admin() -> 'html':
    conn, cur = db_execute()
    cur.execute('''select * from user where g_id not in('admin')''')
    alldata = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("g_admin.html", alldata=alldata)

@ app.route('/g_write/', methods=['POST', 'GET'])  # 담당경로
def g_write_con() -> "html":
    return render_template("g_write.html")


@ app.route('/g_write_result/', methods=['POST'])  # 담당경로
def g_result_con() -> "html":
    a = request.form['u_id']  # g_write에 name
    b = request.form['u_pw']  # g_write에 name
    print(a, b, sep='\n')  # 결과 출력
    conn, cur = db_execute()
    # format을 사용
    SQL = f'INSERT INTO user (g_id,g_pw) value("{a}","{b}");'
    cur.execute(SQL)
    conn.commit()
    cur.close()
    conn.close()
    return render_template("g_write_result.html", id=a, pw=b)


@app.route('/g_write_delete/', methods=['POST', 'GET'])
def g_delete_con():
    return render_template("g_write_delete.html")


@app.route('/g_delete_result/', methods=["POST"])
def g_result_delete():
    a = request.form['u_id']
    conn, cur = db_execute()
    SQL = """DELETE FROM user WHERE g_id = %s"""
    cur.execute(SQL, (a,))
    conn.commit()
    cur.close()
    conn.close()
    return render_template("g_delete_result.html")

@app.route("/read/", methods=['POST', 'GET'])
def g_read():
    return render_template("g_list_read.html")



@app.route("/g_write_update/")
def g_update():
    return render_template("g_write_update.html")

@app.route("/g_result_update/")
def g_result_update():
    a = request.form['u_id']
    b = request.form['u_pw']  # g_write에 name
      # g_write에 name
    conn, cur = db_execute()
    SQL = """UPDATE user SET g_id = %s g_pw  = %s WHERE  g_id = %s g_pw = %s"""
    cur.execute(SQL, (a,b)) 
    conn.commit()
    cur.close()
    conn.close()
    return render_template("g_result_update.html", id=a, pw=b)

app.run(debug=True)

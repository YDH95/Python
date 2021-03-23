import mysql
import mysql.connector
from flask import Flask, render_template, request, session
from mysql.connector import cursor
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "010"  # 고유 비밀키


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')


@app.route('/')
def login() -> 'html':
    id = session.get("user_id", None)
    return render_template("admin_login.html", id=id)


@app.route('/login/', methods=['POST'])  # 로그인처리 담당자
def login_db_con() -> 'html':
    u_id = request.form["user_id"]
    u_pw = request.form["user_pw"]
    dbconfig = {'host': 'localhost', 'user': 'root',
                'password': '', 'database': 'member_db'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    SQL = "SELECT * FROM login_t WHERE id=%s and pw=%s"
    cursor.execute(SQL, (u_id, u_pw))
    alldata = cursor.fetchall()
    cursor.close()
    conn.close()
    info = ''
    if(len(alldata) >= 1):
        if u_id == 'admin':
            return redirect('/admin/')
        print("logged in...")
        session.clear()
        session["user_id"] = u_id
        return redirect('/')
    else:
        print("who are you...")
        return render_template("admin_login.html", info='다시입력해주세요.')


@app.route('/admin/')
def admin() -> 'html':
    dbconfig = {'host': 'localhost', 'user': 'root',
                'password': '', 'database': 'member_db'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    cursor.execute('''select * from login_t where id not in('admin')''')
    alldata = cursor.fetchall()
    cursor.close()
    conn.close()
    print(alldata)
    return render_template("admin.html", alldata=alldata)


app.run(debug=True)

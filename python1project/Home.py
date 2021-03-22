
# 플라스크 프레임워크 모듈로딩
from flask.globals import session
import mysql
import mysql.connector
from flask import Flask, render_template, request, session
# 플라스크 객체생성(모든작업의 기초가되는 물체)
# ==============================

app = Flask(__name__)
app.secret_key = "010"  # 고유 비밀번호


@app.route("/uns")
def uns() -> "html":
    print("ok")
    return render_template("Unsubscribe.html")


@app.route("/log")  # 로그인처리 담당
def log() -> "html":
    return render_template("rogin_page.html")


@app.route("/regcom/", methods=['POST'])
def regcom_page() -> "html":
    u_id = request.form["userID"]
    u_pw = request.form["userPW"]
    c = request.form["userphone"]
    return render_template("regcom_page.html", data=u_id, data2=u_pw, data3=c)


@ app.route("/reg/", methods=['POST'])
def register_page() -> "html":
    return render_template("register_page.html")


@ app.route("/", methods=['POST','GET'])  # http://localhost:5000/
def homepage_page() -> "html":
    return render_template("Home_page.html")


app.run(debug=True)

session.clear()
sessionp[user_id] = userID
sessionp[user_id] = u_id

u_id = request.form['post_id']
u_pw = request.form['post_pw']

dbconfig = {'host': 'localhost', 'user': 'root',
            'password': '', 'database': 'member_db'}
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
SQL = "SELECT * FROM login_t WHERE u_id=%s and u_pw=%s"
# execute 라는 명령어는 자신이 실행한 SQL의 실행결과가 정상인지 아닌지 알려줄수있다.
# 그방벙을 나중에아라내서 저어두세요!(리턴결과)
cursor.execute(SQL, (u_id, u_pw))

alldata = cursor.fetchall()  # 검색된 결과를 모두 가져와라! 그리고 res변수에 저장해줘라.

# 실행결과가 뭔가 있다면, 로그인이 되었다는 얘기고
# 실행결과가 없다면, 그런 유저가 없다는것이다.
# 만약 유저가 있다면 그유저의 정보(ID)를 세션변수에 저장한다.

# 그유저의정보를 출력하라
for rec in alldata:
    print(rec[0])
    print(rec[1])
    print(rec[2])
    print(rec[3])

cursor.close()
conn.close()

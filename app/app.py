from flask import Flask,render_template,request
from models.models import MedicineInfo
from models.database import db_session

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    all_med = MedicineInfo.query.all()
    return render_template("index.html",name=name,all_med=all_med)

@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    all_med = MedicineInfo.query.all()
    return render_template("index.html",name=name,all_med=all_med)

@app.route("/add",methods=["post"])
def add():
    title = request.form["title"]
    time = request.form["time"]
    content = MedicineInfo(title,time)
    db_session.add(content)
    db_session.commit()
    return index()
    

#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)
    
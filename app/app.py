from flask import Flask,render_template,request
from models.models import MedicineInfo
from models.database import db_session
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    all_med = MedicineInfo.query.all()
    return render_template("index.html",name=name,all_med=all_med)



@app.route("/add",methods=["post"])
def add():
    try:
        title = request.form.get("title")
        selected_option = request.form.get("MorN")

        if not title:
            return "タイトルが空です。"

        if selected_option == "night":
            time = "20:00"
        elif selected_option == "morning":
            time = "8:00"
        else:
            morning_content = MedicineInfo(title+' (朝)', "8:00")
            night_content = MedicineInfo(title+' (夜)', "20:00")
            db_session.add(morning_content)
            db_session.add(night_content)
            db_session.commit()
            return index()

        content = MedicineInfo(title, time)
        db_session.add(content)
        db_session.commit()
        return index()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/delete",methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = MedicineInfo.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return index()

#定期的にデータベース内の時刻をチェック
def check_time_and_trigger():
    current_time = datetime.now().strftime("%H:%M")
    all_med = MedicineInfo.query.all()
    for medicine in all_med:
        if medicine.time == current_time:
            #アクションをここに(ここに音を鳴らしたりする機構を作る)
            print(f"{medicine.title}の時間です")#ターミナル上に表示される
    

#スケジューラのセットアップ
scheduler = BackgroundScheduler()
scheduler.add_job(func=check_time_and_trigger,trigger = "interval", seconds=60)
scheduler.start()

#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)
    

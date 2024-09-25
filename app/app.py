from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

# @app.route("/add",methods=["post"])
# def add():
#     title = request.form["title"]
#     time = request.form["time"]
    
    
    



#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)
    
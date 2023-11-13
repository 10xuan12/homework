from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>黃玟瑄網頁</h1>"
    homepage += "<a href=/myweb>黃玟瑄簡介網頁</a><br>"
    homepage += "<a href=/Miss>MIS相關工作介紹</a><br>"
    homepage += "<a href=/work>職涯測驗結果</a><br>"
    homepage += "<a href=/me>求職履歷</a><br>"
    return homepage

@app.route("/myweb")
def myweb():
    return render_template("myweb.html")    

@app.route("/Miss")
def Miss():
    return render_template("Miss.html")    

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/me")
def me():
    return render_template("me.html")

#if __name__ == "__main__":
    #app.run()

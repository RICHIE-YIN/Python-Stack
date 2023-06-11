from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def play():
    return render_template("play.html")  

@app.route('/play/<int:num>')
def playx(num):
    return render_template("playx.html", num= num)   

@app.route('/play/<int:x>/<string:color>')
def playcolor(x, color):
    return render_template("playcolor.html", times=x, color=color)   

if __name__=="__main__":
    app.run(debug=True)

    
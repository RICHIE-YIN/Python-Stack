from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "2pac"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods = ['post'])
def create_users():
    print(request.form)
    session['yourname'] = request.form['yourname']
    session['Location'] = request.form['Location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')


if __name__ =="__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

counter = 0

@app.route('/')
def index():
    global counter
    counter += 1
    return str(counter)

@app.route('/destroy_session')
def destroy():
    global counter
    counter = 0
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
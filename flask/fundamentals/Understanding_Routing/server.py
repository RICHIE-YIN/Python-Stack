from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hi " + name+"!"
    # return f"Hi {name.capitalize()}!"

@app.route('/repeat/<value>/<word>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output
# def repeat(value, word):
#     print(word)
#     return word * value


if __name__=="__main__":   
    app.run(debug=True)    # Run the app in debug mode.
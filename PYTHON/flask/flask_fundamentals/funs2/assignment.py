from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/Champion")
def Champion():
    
    return "Champion"

@app.route("/say/<name>")
def say(name):
    
    return f"Hi {name}!"

@app.route("/repeat/<num>/<name>")
def repeat(num,name):
    
    return  name* int(num)



if __name__ == "__main__":
    app.run(debug=True)

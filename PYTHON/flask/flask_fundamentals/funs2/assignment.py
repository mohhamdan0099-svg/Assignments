from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/Champion")
def Champion():
    
    return "Champion"

@app.route("/say/<name>")
def say(name):
    
    return f"Hi {name}!"

@app.route("/repeat/<num>/<name>")
def repeat(num,name):
    
    return  name * int(num)



if __name__ == "__main__":
    app.run(debug=True)

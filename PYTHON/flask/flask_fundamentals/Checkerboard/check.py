from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def checkboard():
    return render_template("index.html",rows=8,colos=8)

@app.route('/<x>')
def check(x):
    return render_template("index.html",rows=int(x),colos=8)

@app.route('/<x>/<y>')
def checkxy(x,y):
    return render_template("index.html",rows=int(x),colos=int(y))



if __name__ == "__main__":
    app.run(debug=True)

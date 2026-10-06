from flask import Flask,render_template

app = Flask(__name__)


@app.route('/play')
def hello_world():
    return render_template("index.html")

@app.route('/play/<x>/<colorr>')
def hello(x,colorr):

    return render_template("index.html", boxcount=int(x),background_color=colorr )


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def create_user():
    
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    textarea_from_form = request.form['textarea']

    return render_template(
        "show.html",
        name_on_template=name_from_form,
        location_on_template=location_from_form,
        language_on_template=language_from_form,
        textarea_on_template=textarea_from_form,
    )


if __name__ == "__main__":
    app.run(debug=True)
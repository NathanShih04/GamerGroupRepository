# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kurtis/')
def kurtis():
    return render_template("kurtis.html")


@app.route('/nathan/')
def nathan():
    return render_template("nathan.html")

@app.route('/colin/')
def colin():
    return render_template("colin.html")

@app.route('/everitt/')
def everitt():
    return render_template("everitt.html")


@app.route('/jackson/')
def jackson():
    return render_template("jackson.html")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

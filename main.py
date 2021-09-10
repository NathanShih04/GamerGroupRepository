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
            return render_template("greet/greet.html", name=name)
    # starting and empty input default
    return render_template("greet/greet.html", name="World")
@app.route('/jgreet', methods=['GET', 'POST'])
def jgreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet/jacksongreet.html", name=name)
    # starting and empty input default
    return render_template("greet/jacksongreet.html", name="World")
@app.route('/ngreet', methods=['GET', 'POST'])
def ngreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet/nathangreet.html", name=name)
    # starting and empty input default
    return render_template("greet/nathangreet.html", name="World")
@app.route('/egreet', methods=['GET', 'POST'])
def egreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet/everittgreet.html", name=name)
    # starting and empty input default
    return render_template("greet/everittgreet.html", name="World")
@app.route('/cgreet', methods=['GET', 'POST'])
def cgreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet/colingreet.html", name=name)
    # starting and empty input default
    return render_template("greet/colingreet.html", name="World")
@app.route('/kabout/')
def kabout():
    return render_template("about/kurtisabout.html")
@app.route('/eabout/')
def eabout():
    return render_template("about/everittabout.html")
@app.route('/jabout/')
def jabout():
    return render_template("about/jacksonabout.html")
@app.route('/nabout/')
def nabout():
    return render_template("about/nathanabout.html")
@app.route('/cabout/')
def cabout():
    return render_template("about/colinabout.html")

@app.route('/clicker/')
def clicker():
    return render_template("clicker.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

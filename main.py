import json

from flask_restful.inputs import url

2  # import "packages" from flask
from flask import Flask, render_template, request
from image import image_data
import requests
from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Monkey Reaction/')
def monkey():
    return render_template("monkeyreaction/monkeyreaction.html")


@app.route('/Turtle Clicker/')
def turtle():
    return render_template("turtleclicker.html")

@app.route('/Website Generator/')
def website():
    return render_template("website.html")


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


@app.route("/binary/", methods=['GET', 'POST'])
def binary():
    BITS = 8
    imgBulbOn = "/static/turtleon!.png"
    # second time you call it, its a post action
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        imgBulbOn = request.form['lightOn']
    return render_template("clicker.html", imgBulbOn=imgBulbOn, BITS=BITS)


@app.route('/tclicker/')
def tclicker():
    return render_template("turtleclicker.html")


@app.route('/mreaction/')
def mreaction():
    return render_template("monkeyreaction/monkeyreaction.html")


@app.route('/unsignedaddition/')
def unsignedaddition():
    return render_template("/labs/unsignedaddition.html")


@app.route('/rgb/')
def rgb():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('labs/rgb.html', images=image_data(path))


@app.route('/logicgates/')
def logicgates():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('labs/logicgates.html', images=image_data(path))


@app.route("/colorcode/", methods=['GET', 'POST'])
def ccode():
    BITS = 8
    imgBulbOn = "/static/turtleon!.png"
    # second time you call it, its a post action
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        imgBulbOn = request.form['lightOn']
    return render_template("/labs/colorcode.html", imgBulbOn=imgBulbOn, BITS=BITS)

@app.route('/marine/',methods=['GET','POST'])
def study():

    url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"
    querystring = {"category":"sciencenature","limit":"1"}
    headers = {
        'x-rapidapi-host': "trivia-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    output = json.loads(response.text)
    return render_template('labs/marine.html', question=output)
@app.route('/website/')
def web():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('labs/website.html', images=image_data(path))

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

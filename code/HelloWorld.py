from flask import Flask
app = Flask(__name__)
from flask import render_template, request, redirect

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def data():
    if request.method == "POST":

        req = request.form
        print(req)
        return redirect(request.url)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

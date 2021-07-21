from flask import Flask
app = Flask(__name__)
from flask import render_template, request, redirect

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":

        abyss9 = request.form.get("abyss9")
        print(abyss9)
        days = request.form.get("numdays")
        print(days)
        #return redirect(request.url)
    return render_template("results.html", abyss9=abyss9, days=days)

if __name__ == '__main__':
    app.run(debug=True)
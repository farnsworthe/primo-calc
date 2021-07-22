from flask import Flask
app = Flask(__name__)
from flask import render_template, request, redirect

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":

        # checkbox boolean variables
        mnEvtCheck, mtlvCheck, dlyCheck, trCheck, wlknCheck, bpCheck = False, False, False, False, False, False

        # retrieving form data
        patches = 0
        abyssCycles = 0

        days = int(request.form.get("numdays"))

        abyss9 = request.form.get("abyss9")
        abyss10 = request.form.get("abyss10")
        abyss11 = request.form.get("abyss11")
        abyss12 = request.form.get("abyss12")

        if request.form.get("main_event"):
            mnEvtCheck = True
        sideEvt = request.form.get("side_event")
        newQuests = request.form.get("new_quests")

        if request.form.get("maint_live"):
            mtlvCheck = True
        if request.form.get("dailies"):
            dlyCheck = True
        if request.form.get("test_runs"):
            trCheck = True

        if request.form.get("welkin"):
            wlknCheck = True
        if request.form.get("bp"):
            bpCheck = True
        paid = request.form.get("paid")

        # declaring calc variables
        abyssP = 0
        dailiesP = 0
        welkinP = 0

        # calculations
        if dlyCheck:
            dailiesP = days * 60
        if wlknCheck:
            welkinP = days * 90

        # adding to the total
        total = 0
        total = dailiesP + welkinP

    return render_template ("results.html",
        days=days, total=total,
        abyssP=abyssP, dailiesP=dailiesP, welkinP=welkinP
    )

if __name__ == '__main__':
    app.run(debug=True)
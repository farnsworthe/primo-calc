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
        abyssCycles = 1

        days = int(request.form.get("numdays"))

        ##########

        abyss9 = 0
        abyss10 = 0
        abyss11 = 0
        abyss12 = 0
        
        if request.form.get("abyss9"):
            abyss9 = int(request.form.get("abyss9"))
        if request.form.get("abyss10"):
            abyss10 = int(request.form.get("abyss10"))
        if request.form.get("abyss11"):
            abyss11 = int(request.form.get("abyss11"))
        if request.form.get("abyss12"):
            abyss12 = int(request.form.get("abyss12"))

        ##########

        if request.form.get("main_event"):
            mnEvtCheck = True
        sideEvt = request.form.get("side_event")
        newQuests = request.form.get("new_quests")

        ##########

        if request.form.get("maint_live"):
            mtlvCheck = True
        if request.form.get("dailies"):
            dlyCheck = True
        if request.form.get("test_runs"):
            trCheck = True

        ##########
        
        paid = 0

        if request.form.get("welkin"):
            wlknCheck = True
        if request.form.get("bp"):
            bpCheck = True
        if request.form.get("paid"):
            paid = int(request.form.get("paid"))

        # declaring calc variables
        dailiesP = 0
        welkinP = 0

        # calculations
        abyss9P = (abyss9//3) * 50 
        abyss10P = (abyss10//3) * 50 
        abyss11P = (abyss11//3) * 50
        abyss12P = (abyss12//3) * 50
        abyssP = abyssCycles * (abyss9P + abyss10P + abyss11P + abyss12P)

        if dlyCheck:
            dailiesP = days * 60
        if wlknCheck:
            welkinP = days * 90

        # adding to the total
        total = abyssP + dailiesP + welkinP + paid

    return render_template("results.html", 
        days=days, 
        abyss9P=abyss9P, abyss10P=abyss10P, abyss11P=abyss11P, abyss12P=abyss12P, abyssP=abyssP,
        dailiesP=dailiesP,
        welkinP=welkinP, paid=paid,
        total=total)

if __name__ == '__main__':
    app.run(debug=True)
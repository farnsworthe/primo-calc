from flask import Flask
app = Flask(__name__)
from flask import render_template, request, redirect
import datetime 

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
        abyssCycles = 1
        patchCount = 0

        # dates
        days = int(request.form.get("numdays"))
        startDate = request.form.get("start")
        endDate = request.form.get("end")
        startdate_object = datetime.datetime.strptime(startDate, "%Y-%m-%d")
        enddate_object = datetime.datetime.strptime(endDate, "%Y-%m-%d")

        list = []

        list.append(datetime.datetime(int(2021), int(8), int(31)))
        list.append(datetime.datetime(int(2021), int(10), int(12)))
        list.append(datetime.datetime(int(2021), int(11), int(23)))
        list.append(datetime.datetime(int(2022), int(1), int(4)))
        list.append(datetime.datetime(2022, 2, 15))
        list.append(datetime.datetime(2022, 3, 29))
        list.append(datetime.datetime(2022, 5, 10))
        list.append(datetime.datetime(2022, 6, 21))
        list.append(datetime.datetime(2022, 8, 2))
        list.append(datetime.datetime(2022, 9, 13))
        list.append(datetime.datetime(2022, 10, 25))
        list.append(datetime.datetime(2022, 12, 6))
        list.append(datetime.datetime(2023, 1, 17))
        list.append(datetime.datetime(2023, 2, 28))
        list.append(datetime.datetime(2023, 5, 23))
        list.append(datetime.datetime(2023, 7, 4))
        list.append(datetime.datetime(2023, 8, 15))
        list.append(datetime.datetime(2023, 9, 26))
        list.append(datetime.datetime(2023, 11, 7))
        list.append(datetime.datetime(2023, 12, 19))

        list_length = len(list)

        for i in range(list_length):
            if (startdate_object <= list[i] <= enddate_object):
                patchCount += 1
            else:
                break


        print(patchCount)
    

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

        # abyss primos


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
        pulls = total//160

        # sum values
        eventsP = 0 # <-- temp value, change to sum of parameters
        miscP = dailiesP #+ maint&live + test runs
        paidP = welkinP #+ bp + crystals

    return render_template("results.html", 
        days=days,
        abyss9=abyss9, abyss10=abyss10, abyss11=abyss11, abyss12=abyss12,
        abyss9P=abyss9P, abyss10P=abyss10P, abyss11P=abyss11P, abyss12P=abyss12P, abyssP=abyssP,
        eventsP=eventsP,
        dailiesP=dailiesP, miscP=miscP,
        welkinP=welkinP, paid=paid, paidP=paidP,
        total=total, pulls=pulls)

if __name__ == '__main__':
    app.run(debug=True)
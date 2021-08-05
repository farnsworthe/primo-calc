from flask import Flask
app = Flask(__name__)
from flask import render_template, request, redirect
import datetime 
from dateutil.relativedelta import *

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
        patchCount = 1

        # dates
        days = int(request.form.get("numdays"))
        startDate = request.form.get("start")
        endDate = request.form.get("end")
        startdate_object = datetime.datetime.strptime(startDate, "%Y-%m-%d")
        enddate_object = datetime.datetime.strptime(endDate, "%Y-%m-%d")
        abyss1 = startdate_object
        abyss2 = startdate_object

        # finding the next two dates in abyss
        if int(startdate_object.day) > 1:
            abyss1 = abyss1 + relativedelta(months=+1)
            abyss1.day = 1
        if int(startdate_object.day) > 16:
            abyss2 = abyss2 + relativedelta(months=+1)
            abyss2.day = 16
        else:
            abyss2.day = 16

        print(abyss1)
        print(abyss2)


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
            if startdate_object <= list[i] <= enddate_object:
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

        sideEvt = 0
        newQuests = 0

        if request.form.get("main_event"):
            mnEvtCheck = True
        if request.form.get("side_event"):
            sideEvt = int(request.form.get("side_event"))
        if request.form.get("new_quests"):
            newQuests = int(request.form.get("new_quests"))

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
        mnEvtP = 0
        sideEvtP = 0
        newQuestsP = 0
        dailiesP = 0
        mainliveP = 0
        testrunP = 0
        welkinP = 0
        bpP = 0
        bpFates = 0

        # calculations
        abyss9P = (abyss9//3) * 50 
        abyss10P = (abyss10//3) * 50 
        abyss11P = (abyss11//3) * 50
        abyss12P = (abyss12//3) * 50
        abyssP = abyssCycles * (abyss9P + abyss10P + abyss11P + abyss12P)

        if dlyCheck:
            dailiesP = days * 60
        if mtlvCheck:
            mainliveP = patchCount * 600
        if trCheck:
            testrunP = patchCount * 40
        if wlknCheck:
            welkinP = days * 90
        if bpCheck:
            bpP = patchCount * 680
            bpFates = patchCount * 4
        if mnEvtCheck:
            mnEvtP = patchCount * 872

        sideEvtP = patchCount * sideEvt * 413
        newQuestsP = patchCount * newQuests * 60

        # adding to the total
        total = abyssP + mnEvtP + sideEvtP + newQuestsP + dailiesP + mainliveP + testrunP + welkinP + bpP + (bpFates * 160) + paid
        pulls = total//160

        # sum values
        eventsP = mnEvtP + sideEvtP + newQuestsP 
        miscP = dailiesP + mainliveP + testrunP 
        paidP = welkinP + bpP + (bpFates * 160) + paid

    return render_template("results.html", 
        days=days,
        abyss9=abyss9, abyss10=abyss10, abyss11=abyss11, abyss12=abyss12,
        abyss9P=abyss9P, abyss10P=abyss10P, abyss11P=abyss11P, abyss12P=abyss12P, abyssP=abyssP,
        mnEvtP=mnEvtP, sideEvtP=sideEvtP, newQuestsP=newQuestsP, eventsP=eventsP,
        dailiesP=dailiesP, mainliveP = mainliveP, testrunP = testrunP, miscP=miscP,
        welkinP=welkinP, bpP = bpP, bpFates = bpFates, paid=paid, paidP=paidP,
        total=total, pulls=pulls)

if __name__ == '__main__':
    app.run(debug=True)
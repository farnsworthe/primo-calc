window.onload = function () {
    if (!sessionStorage.getItem('popUp')){
        setTimeout(function () {
            popUp('show');
        }, 10);
    }
    sessionStorage.setItem('popUp', 'true');
}

function popUp(hideOrshow) {
    if (hideOrshow == 'hide') document.getElementById('popwrap').style.display = "none";
    else document.getElementById('popwrap').removeAttribute('style');
}

function GetDays() {
    var enddt = new Date(document.getElementById("end").value);
    var startdt = new Date(document.getElementById("start").value);
    return parseInt((enddt - startdt) / (24 * 3600 * 1000));
}

function cal() {
    if(document.getElementById("end")) {
    document.getElementById("numdays2").value=GetDays();
    }
    updateMin();  
}

function updateMin(){
    document.getElementById("end").min = document.getElementById("start").value;
}

function vadliate(){
    var days = document.getElementById("numdays2").value;
    if (days < 1)
        return false;
}

function fillBlanks() {
    document.getElementById('abyss9').value=9;
    document.getElementById("abyss10").value=9;
    document.getElementById("abyss11").value=0;
    document.getElementById("abyss12").value=0;

    document.getElementById("main_event").checked = true;
    document.getElementById("side_event").value=3;
    document.getElementById("new_quests").value=2;

    document.getElementById("dailies").checked = true;
    document.getElementById("maint_live").checked = true;
    document.getElementById("test_runs").checked = true;
}
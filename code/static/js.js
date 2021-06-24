function GetDays() {
    var enddt = new Date(document.getElementById("end").value);
    var startdt = new Date(document.getElementById("start").value);
    return parseInt((enddt - startdt) / (24 * 3600 * 1000));
}

function cal() {
    if(document.getElementById("end")) {
    document.getElementById("numdays2").value=GetDays();
    }  
}
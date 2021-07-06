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

function hideIntro() {
    var x = document.getElementById('intro');
    if (x.style.display = "block") {
        x.style.display = "none";
    }
}

function displayTab(element) {
    var tabContents = document.getElementsByClassName('tabContent');
    for (var i = 0; i < tabContents.length; ++i) {
        tabContents[i].style.display = 'none';
    }
    var tabContentIdToShow = element.id.replace(/(\d)/g, '-$1');
    document.getElementById(tabContentIdToShow).style.display = 'block';
}
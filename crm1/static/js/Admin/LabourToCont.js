var n =  new Date();
var y = n.getFullYear();
var m = n.getMonth() + 1;
var d = n.getDate();
document.getElementById("date").innerHTML = d + "/" + m + "/" + y;


function goBack(){ 
    location.replace("../admin.php?v="+n.getTime()+"&n="+document.getElementById("nam").innerHTML+"&l="+document.getElementById("area").innerHTML);
};
document.querySelector(".bkbtn").addEventListener("click",goBack);
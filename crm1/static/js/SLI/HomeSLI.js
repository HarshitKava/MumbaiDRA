var n =  new Date();
var y = n.getFullYear();
var m = n.getMonth() + 1;
var d = n.getDate();
document.getElementById("date").innerHTML = d + "/" + m + "/" + y;

function goBack(){ 
    location.replace("../index.php?v="+n.getTime());
};
document.querySelector(".bkbtn").addEventListener("click",goBack);

function checkpass(){ 
    location.replace("Report/form.php?v="+n.getTime()+"&n="+document.getElementById("nam").innerHTML+"&l="+document.getElementById("area").innerHTML);
};
document.querySelector(".addbtn").addEventListener("click",checkpass);
function nightReport(){ 
    location.replace("ShowData/form.php?v="+n.getTime()+"&n="+document.getElementById("nam").innerHTML+"&l="+document.getElementById("area").innerHTML);
};
document.querySelector(".showbtn").addEventListener("click",nightReport);

function myFunction() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}
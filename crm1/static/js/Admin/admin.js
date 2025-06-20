var n =  new Date();
var y = n.getFullYear();
var m = n.getMonth() + 1;
var d = n.getDate();
document.getElementById("date").innerHTML = d + "/" + m + "/" + y;

// function goBack(){ 
//     location.replace("../index.php?v="+n.getTime());
// };
// document.querySelector(".bkbtn").addEventListener("click",goBack);

// function addUser() {
//     location.replace("User/User.php?v="+n.getTime()+"&n="+document.getElementById("nam").innerHTML+"&l="+document.getElementById("area").innerHTML);
// }
// document.querySelector(".addSE").addEventListener("click",addUser);

// function resetPass() {
//     location.replace("Reset/reset.php?v="+n.getTime()+"&n="+document.getElementById("nam").innerHTML+"&l="+document.getElementById("area").innerHTML);
// }
// document.querySelector(".reset").addEventListener("click",resetPass);

// function addContractor() {
//     location.replace("Contractor/contractor.php?v="+n.getTime()+"&n="+document.getElementById("nam").innerHTML+"&l="+document.getElementById("area").innerHTML);
// }
// document.querySelector(".addCont").addEventListener("click",addContractor);

// function addTypeOfLabour() {
//     location.replace("TypeOfLabor/typeOfLabor.php?v="+n.getTime()+"&n="+document.getElementById("nam").innerHTML+"&l="+document.getElementById("area").innerHTML);
// }
// document.querySelector(".addCat").addEventListener("click",addTypeOfLabour);




function myFunction() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}
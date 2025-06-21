var n =  new Date();
var y = n.getFullYear();
var m = n.getMonth() + 1;
var d = n.getDate();
setPass();
function setPass(){
    // change type to text
    document.getElementById("id_email").autocomplete="on";
    // add required attribute
    document.getElementById("id_email").required=true;
    console.log(document.getElementById("id_email").value);
    document.getElementById("id_password1").value="Pass@123";
    document.getElementById("id_password2").value="Pass@123";
    document.getElementById("id_groups").removeAttribute("multiple");
    document.getElementById("id_username").innerHTML="Name";
}
document.getElementById("id_username").addEventListener('input',inputHandler);
function inputHandler(e) {
    document.getElementById("id_Username").value=e.target.value;
}

function confirmPass() {
    var pass=document.getElementById('Pass');
    var x=document.getElementById('ConPass');
    if (pass.value=="" || x.value==""){
        document.getElementById("errormsg").style.color="orange";
        document.getElementById("errormsg").innerHTML="Password not entered";
    }
    else if(pass.value==x.value){
        document.getElementById("errormsg").style.color="green";
        document.getElementById("errormsg").innerHTML="Passwords are same.";
    }
    else{
        document.getElementById("errormsg").style.color="red";
        document.getElementById("errormsg").innerHTML="Passwords are not same.";
    }
}

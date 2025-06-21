window.onload = function() {
    try{
        var q = document.getElementById("ar_id").innerHTML;
        document.getElementById("id_Areaname").value = q;
    }
    catch(err){
        console.log("No Area Name");
    }
    // Set Width of ul with class nav
    // var nav = document.getElementsByClassName("nav");
    // var table = document.getElementById("display");
    // var table_width = table.offsetWidth;
    // nav[0].style.width = table_width + "px";
    
    // get the width of the table
    // var table = document.getElementById("display");
    
    // console.log(table_width);
    // console.log(nav[0].style.width,table_width);
}


